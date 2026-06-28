import streamlit as st
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model
import pandas as pd 
import numpy as np

#load model
model = load_model("ckd_ann_model.h5")

st.title("chronic kidney disease predicter using ANN")

################# User Details #########################

user_age = st.number_input("Enter your age", 0, 130, 25)

creatinine_level = st.number_input("Enter creatine level (mg/dL)")

bun = st.number_input("Enter urea nitrogen amount of blood:(BUN) (mg/dL)")

input_diabetes = st.radio(
    "does you have diabetes?",
    ["Yes, I have.","No, I haven't"]
)

is_diabetes = 0
if input_diabetes == "Yes, I have." : is_diabetes = 1


input_hypertention = st.radio(
    "does you have hypertention?",
    ["Yes, I have.","No, I haven't"]
)
is_hypertention = 0
if input_hypertention == "Yes, I have." : is_hypertention = 1

urine_output = st.number_input("Enter urine output (ml/day).")

gfr = st.number_input("Enter Glomerular Filtration Rate : (GFR)")

user_input = {
    "Age" : user_age ,
    "Creatinine_Level" : creatinine_level ,
    "BUN" : bun, 
    "Diabetes" : is_diabetes, 
    "Hypertension": is_hypertention,
    "GFR" : gfr ,
    "Urine_Output" : urine_output ,
}


################# input_preprocess #########################

input_df = pd.DataFrame([user_input])

scaler = joblib.load("scaler.pkl")
input_df_scaled = scaler.transform(input_df)


################# model prediction #########################

prediction = model.predict(input_df_scaled)
result = prediction[0][0]


if result > 0.5 :
    st.write("**:red[sorry , you have higher chances of CKD.]**")
else :
    st.write("**:green[hurrraay , you have low chances of CKD.]**")

st.write("probability of CKD :",result)









