from sklearn.model_selection import train_test_split
from utils import Utils
from sklearn.preprocessing import StandardScaler
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


class Preprocess:
    def loadData(filename):
        print("Hello, world! " + filename)
        # Data Initialising, Importing
        df = pd.read_csv(filename)
        df.info()
        # We can also check for null values in the dataset.
        df.isna().sum()

        # Dealing thee  missing values like the length and depth with the mean.

        df["culmen_length_mm"] = df["culmen_length_mm"].fillna(value=df["culmen_length_mm"].mean())
        df["culmen_depth_mm"] = df["culmen_depth_mm"].fillna(value=df["culmen_depth_mm"].mean())
        df["flipper_length_mm"] = df["flipper_length_mm"].fillna(value=df["flipper_length_mm"].mean())
        df["body_mass_g"] = df["body_mass_g"].fillna(value=df["body_mass_g"].mean())

        # Dealing with missing values in sex
        df['sex'] = df['sex'].fillna('MALE')
        df[df['sex'] == '.']
        df.loc[336, 'sex'] = 'MALE'
        df

        # CHecking whether there are anymore missing values
        df.isna().sum()

        df.describe()

        df['species'].value_counts()

        # Preprocess.visualizeIT( df)

        #  COnverting text into numemrical values
        dgender = {'MALE': 0, 'FEMALE': 1}
        dspecies = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
        disland = {'Torgersen': 0, 'Biscoe': 1, 'Dream': 2}
        newdf = df.copy()
        newdf['species'] = df['species'].map(dspecies)
        newdf['island'] = df['island'].map(disland)
        newdf['sex'] = df['sex'].map(dgender)

        X = newdf.drop(['sex'], axis='columns')
        y = newdf["sex"]

        # Creating an File
        Utils.saveToCsv("../data/Iris_X.csv", X)
        Utils.saveToCsv("../data/Iris_y.csv", y)

        #  Creating Dataset for training and testing from test.csv using train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

        # Creating an File
        Utils.saveToCsv("../data/Train_Iris_X.csv", pd.DataFrame(X_test))
        Utils.saveToCsv("../data/Train_Iris_y.csv", pd.DataFrame(y_test))

        Utils.saveToCsv("../data/Test_Iris_X.csv", pd.DataFrame(X_train))
        Utils.saveToCsv("../data/Test_Iris_y.csv", pd.DataFrame(y_train))

        scaler = StandardScaler()
        scaler.fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)

        return X_train, X_test, y_train, y_test
