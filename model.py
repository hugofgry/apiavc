import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from data import Data

d = Data()

class Model :

    oht = OneHotEncoder(handle_unknown='ignore')
    X = oht.fit_transform(d.X)

    X_train, X_test, y_train, y_test = train_test_split(X, d.y, test_size=0.3, random_state=1)

    model = LogisticRegression(random_state=0).fit(X_train, y_train)
    

    def predict(self, gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status):
        predic = pd.DataFrame({"gender": [gender], "age":[age], "hypertension":[hypertension],"heart_disease":[heart_disease],"ever_married": [ever_married],"work_type":[work_type],"Residence_type":[Residence_type],"avg_glucose_level": [avg_glucose_level],"bmi":[bmi],"smoking_status":[smoking_status]})
        pred_oht = self.oht.transform(predic)
        pred = self.model.predict_proba(pred_oht)
        result = pred[0][1]*100
        return np.around(result, 2)





