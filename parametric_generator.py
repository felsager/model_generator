import os
print(os.getcwd())
''' Class to generate a ROV SDF model parametrically'''
class RovModelSDF:
    def __init__(self, w_box, l_box, h_box):
        self.w_box = w_box
        self.l_box = l_box
        self.h_box = h_box
        self.m_box = w_box*l_box*h_box*1000 - 0.006# mass of the box is set to achieve neutral buoyancy
        self.I_box = self.calculate_box_inertia() # [I_x, I_y, I_z]
        self.l_thruster = 0.112
        self.r_thruster = 0.039

        self.model_v = self.get_pre_model_v()
        self.update_model_v()
        self.model_name = "rov_model_" + self.model_v
        self.model_path = "models/" + self.model_name
        self.model_sdf_path = self.model_path + "/" + self.model_name + ".sdf"      
        self.model_config_path = self.model_path + "/" + self.model_name + ".config"
        
        self.create_model_dir()
        self.create_model_config()


        self.create_model_sdf()

    "Create the model directory"
    def create_model_dir(self):
        if not os.path.exists("models"):
            os.mkdir("models")
        os.mkdir(self.model_path)

    def create_model_config(self):
        with open(self.model_config_path, "w") as model_config_file:
            with open("templates/config_template", "r") as config_template:
                model_config_file.write(config_template.read().replace("<version>1.0", "<version>" + str(self.model_v) + ".0"))

    "Create the model SDF file"
    def create_model_sdf(self):
        print("Creating model SDF file")
        I = self.calculate_box_inertia()
        p_z = -self.h_box/2 # z position of the box
        p_side_y = self.l_box/2 + self.r_thruster # y position of the side thrusters
        p_up_x = self.w_box/2 + self.r_thruster # x position of the up thrusters
        p_up_y = self.l_box/2 - self.r_thruster # y position of the up thrusters
        with open(self.model_sdf_path, "w") as model_file:
            with open("templates/model_template", "r") as model_template:
                model_template = model_template.read()
                model_template = model_template.replace("p_z", str(p_z))
                model_template = model_template.replace("p_side_y", str(p_side_y))
                model_template = model_template.replace("p_up_x", str(p_up_x))
                model_template = model_template.replace("p_up_y", str(p_up_y))
                model_template = model_template.replace("I_x", str(I[0]))
                model_template = model_template.replace("I_y", str(I[1]))
                model_template = model_template.replace("I_z", str(I[2]))
                model_template = model_template.replace("m_box", str(self.m_box))
                model_template = model_template.replace("w_box", str(self.w_box))
                model_template = model_template.replace("l_box", str(self.l_box))
                model_template = model_template.replace("h_box", str(self.h_box))
                model_template = model_template.replace("l_thruster", str(self.l_thruster))
                model_template = model_template.replace("r_thruster", str(self.r_thruster))
                model_file.write(model_template)

    " Calculate the inertia of the box "
    def calculate_box_inertia(self):
        I_x = (1/12) * self.m_box * (self.h_box**2 + self.l_box**2)
        I_y = (1/12) * self.m_box * (self.h_box**2 + self.w_box**2)
        I_z = (1/12) * self.m_box * (self.l_box**2 + self.w_box**2)
        return [I_x, I_y, I_z]

    "Get the model version from the model_version file"
    def get_pre_model_v(self):
        if not os.path.exists("model_version"):
            with open("model_version", "w") as model_v_file:
                model_v_file.write("0")
        with open("model_version", "r") as model_v_file:
            model_v = model_v_file.read()
        return model_v
    
    "Update the model version in the model_version file"
    def update_model_v(self):
        with open("model_version", "w") as model_v_file:
            self.model_v = str(int(self.model_v) + 1)
            model_v_file.write(self.model_v)
        
