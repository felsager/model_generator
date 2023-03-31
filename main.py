import parametric_generator as pg

def main():
    rov_model_sdf = pg.RovModelSDF(0.3, 0.3, 0.2)
    print(rov_model_sdf.model_v)

if __name__ == "__main__":
    main()