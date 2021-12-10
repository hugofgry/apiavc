import pandas as pd
from Database import Databases

a = Databases()


class Data() :

    def manip(self):

        df_avc = pd.read_sql("SELECT * FROM avc;", a.engine)
        df_avc.dropna(inplace=True)

        y = df_avc['stroke']
        X = df_avc.drop(['stroke','id','index'], axis=1)

        return X, y

