import psycopg2 as psp
import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine

get_data = pd.read_csv("data/healthcare-dataset-stroke-data.csv", sep= ",")


class Databases :

    def __init__(self):

        self.engine = create_engine('postgresql+psycopg2://hugofugeray:postgres@localhost/avc')









    def create_table(self):

        self.engine.execute("""DROP TABLE avc""")
        self.engine.execute("""CREATE TABLE IF NOT EXISTS avc (id INTEGER, gender VARCHAR(255),age INTEGER, hypertension INTEGER,	heart_disease INTEGER, ever_married VARCHAR(255),work_type VARCHAR(255),Residence_type VARCHAR(255),	avg_glucose_level REAL, 	bmi REAL ,smoking_status VARCHAR(255) ,	stroke INTEGER)""")
        return 'table créée'




    def inserting(self):

        get_data.to_sql('avc', self.engine, if_exists='replace')


