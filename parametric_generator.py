import os
print(os.getcwd())
''' Class to generate a ROV SDF model parametrically'''
class RovModelSDF:
    def __init__(self, w_box, l_box, h_box, m_box):
        self.w_box = w_box
        self.l_box = l_box
        self.h_box = h_box
        self.m_box = m_box
        self.l_thruster = 0.112
        self.r_thruster = 0.039
        self.m_thruster = 0

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

    def create_box_pose(self):
        return "0 0 0 0 0 0"
    
    def create_side_thruster_poses(self):
        return "0 0 0 0 0 0"
    
    def create_vertical_thruster_poses(self):
        return "0 0 0 0 0 0"

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
        
