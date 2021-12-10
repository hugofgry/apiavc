from fastapi import FastAPI, Path, HTTPException
from model import Model



app = FastAPI(title="AVC")
a= Model()

@app.get("/prediction")
async def predict(gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status):

    gender = str(gender)
    age = int(age)
    hypertension = int(hypertension)
    heart_disease = int(heart_disease)
    ever_married = str(ever_married)
    work_type = str(work_type)
    Residence_type = str(Residence_type)
    avg_glucose_level = int(avg_glucose_level)
    bmi = int(bmi)
    smoking_status = str(smoking_status)


    return  Model().predict(gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status)


