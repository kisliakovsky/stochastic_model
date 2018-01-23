from src.model import MongooseModel, AltMongooseModel
from src import exporting


def main():
    model1 = MongooseModel(30, 0.427, 0.001, 6300, 1979, 2000)
    model2 = MongooseModel(6141, 0.427, 0.6, 6300, 2000, 2011)
    model3 = AltMongooseModel(6141, 542.9, 2000, 2011)
    exporting.save_complex_model_plot(model1, model2, model3)


if __name__ == '__main__':
    main()
