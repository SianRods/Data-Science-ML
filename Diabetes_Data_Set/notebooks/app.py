import streamlit as st
import numpy as np
import joblib

# Load the trained SVM model and scaler
model = joblib.load('diabetes_svm_model.pkl')
scaler = joblib.load('data_scaler.pkl')

st.title("Diabetes Prediction App")

# Collect user input features
age = st.number_input('Age', min_value=1, max_value=120, value=25)
glucose = st.number_input('Glucose', min_value=0, max_value=200, value=120)
bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, value=25.0)
blood_pressure = st.number_input('Blood Pressure (Diastolic)', min_value=0, max_value=200, value=80)
diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5)

# Prepare the input data for the model
input_data = np.array([[glucose, blood_pressure, bmi, diabetes_pedigree, age]])

# Scale the input data
input_data_scaled = scaler.transform(input_data)

# Make a prediction
prediction = model.predict(input_data_scaled)

# Output the result
if st.button('Predict'):
    if prediction[0] == 1:
        st.success('The person is diabetic.')
    else:
        st.success('The person is not diabetic.')
