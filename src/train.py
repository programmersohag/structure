# Import modules and packages
# Algorithm Related Initialisation
import warnings
import numpy as np
import pickle
from sklearn.model_selection import GridSearchCV
# FOr KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
from logger import Logger

warnings.filterwarnings('ignore')
#  Constants
modelfilepathwithName = "" + 'finalized_model.pickle'


class Train:
    def trainModel(X_train, X_test, y_train, y_test):
        #  Hyperparameter Tunning in GaussianNB using GridSearchCV
        params_NB = {'var_smoothing': np.logspace(0, -9, num=100)}

        # Usage og Hyper parameter with Cross checking valuei.e CV=5
        kNeighbors_classifier = KNeighborsClassifier()
        k_range = list(range(1, 31))
        param_grid = dict(n_neighbors=k_range)
        KNeighbors_classifierModel = GridSearchCV(kNeighbors_classifier, param_grid, cv=10, scoring='accuracy',
                                                  return_train_score=False, verbose=1)
        KNeighbors_classifierModel

        KNeighbors_classifierModel.fit(X_train, y_train)

        # save the model to disk
        # joblib.dump(KNeighbors_classifierModel, modelfilepathwithName)
        # save model
        pickle.dump(KNeighbors_classifierModel, open(modelfilepathwithName, "wb"))

        Logger.logDebug("Sucessfully Trained")
        return KNeighbors_classifierModel
