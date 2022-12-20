# Import modules and packages
import pickle
import warnings

import pandas as pd
from sklearn import metrics

from logger import Logger
from utils import Utils

warnings.filterwarnings('ignore')

#  Constants
modelfilepathwithName = "" + 'finalized_model.pickle'


class Predict:
    def predictModel(X_test, y_test):
        # Loading the save Model

        loaded_model_KNeighbors = pickle.load(open(modelfilepathwithName, "rb"))

        train_y_Prediction_KNeighbors = loaded_model_KNeighbors.predict(X_test)
        # train_y_Prediction_KNeighbors
        print(train_y_Prediction_KNeighbors)

        # #  Seeing the accuracy level of the algorithm and models
        print(metrics.accuracy_score(y_test, train_y_Prediction_KNeighbors))

        Utils.saveToCsv("../data/result.csv", pd.DataFrame(train_y_Prediction_KNeighbors))

        Utils.saaveToSqlite(pd.DataFrame(train_y_Prediction_KNeighbors))
        Logger.logDebug("Sucessfully Generated Result")
