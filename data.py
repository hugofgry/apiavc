import pandas as pd 

class Data : 
    
    df_avc = pd.read_csv("data/healthcare-dataset-stroke-data.csv", sep= ",")
    df_avc.dropna(inplace=True)
    y = df_avc['stroke']
    X = df_avc.drop(['stroke','id'], axis=1)