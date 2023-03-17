import parametric_generator as pg

def main():
    rov_model_sdf = pg.RovModelSDF(1, 2, 3, 4)
    print(rov_model_sdf.model_v)

if __name__ == "__main__":
    main()