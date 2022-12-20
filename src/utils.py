import numpy as np
import pandas as pd
#  Saving the above dataframe into sqllite
import sqlite3


class Utils:
    def saveToCsv(filename, pfData):
        pfData.to_csv(filename, index=False)

    def saaveToSqlite(pfData):
        # Create a connection to the SQLite database
        # Doesn't matter if the database does not yet exist
        conn = sqlite3.connect('../data/database.sqlite')
        returnStatus = pfData.to_sql('test', conn, if_exists='replace', index=False)
        conn.close()

        return returnStatus
