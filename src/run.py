from predict import Predict
from preprocess import Preprocess
from train import Train

# import preprocess as Preprocess

filename = "../data/Iris.csv"


class Run(object):
    def run(self):
        X_train, X_test, y_train, y_test = Preprocess.loadData(filename)
        Train.trainModel(X_train, X_test, y_train, y_test);
        Predict.predictModel(X_test, y_test)


if __name__ == '__main__':
    Run().run()
