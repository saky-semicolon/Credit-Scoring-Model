import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the saved model
model = joblib.load('credit_scoring_model.pkl')

# Load pre-trained encoders and scaler (if you saved them)
label_encoder_home = LabelEncoder()
label_encoder_intent = LabelEncoder()
label_encoder_grade = LabelEncoder()
label_encoder_default = LabelEncoder()
scaler = StandardScaler()

# Pretrained classes for encoders (manually add from your dataset)
home_classes = ['MORTGAGE', 'RENT', 'OWN', 'OTHER']
intent_classes = ['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION']
grade_classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
default_classes = ['N', 'Y']

# Fit encoders with classes
label_encoder_home.fit(home_classes)
label_encoder_intent.fit(intent_classes)
label_encoder_grade.fit(grade_classes)
label_encoder_default.fit(default_classes)

# Streamlit App
st.title("Credit Scoring Model - Creditworthiness Prediction")

st.sidebar.header("Enter Applicant Details")

# Input fields for user
person_age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)
person_income = st.sidebar.number_input("Annual Income ($)", min_value=5000, max_value=500000, value=50000, step=1000)
person_home_ownership = st.sidebar.selectbox("Home Ownership", options=home_classes)
person_emp_length = st.sidebar.number_input("Employment Length (Years)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)
loan_intent = st.sidebar.selectbox("Loan Intent", options=intent_classes)
loan_grade = st.sidebar.selectbox("Loan Grade", options=grade_classes)
loan_amnt = st.sidebar.number_input("Loan Amount ($)", min_value=500, max_value=500000, value=10000, step=100)
loan_int_rate = st.sidebar.number_input("Loan Interest Rate (%)", min_value=0.0, max_value=50.0, value=12.5, step=0.1)
loan_percent_income = loan_amnt / person_income
cb_person_default_on_file = st.sidebar.selectbox("Default on File", options=default_classes)
cb_person_cred_hist_length = st.sidebar.number_input("Credit History Length (Years)", min_value=0, max_value=50, value=5)

# Preprocess input data
new_data = pd.DataFrame({
    'person_age': [person_age],
    'person_income': [person_income],
    'person_home_ownership': [label_encoder_home.transform([person_home_ownership])[0]],
    'person_emp_length': [person_emp_length],
    'loan_intent': [label_encoder_intent.transform([loan_intent])[0]],
    'loan_grade': [label_encoder_grade.transform([loan_grade])[0]],
    'loan_amnt': [loan_amnt],
    'loan_int_rate': [loan_int_rate],
    'loan_percent_income': [loan_percent_income],
    'cb_person_default_on_file': [label_encoder_default.transform([cb_person_default_on_file])[0]],
    'cb_person_cred_hist_length': [cb_person_cred_hist_length]
})

# Scale numerical features
numerical_features = ['person_age', 'person_income', 'loan_amnt', 
                       'loan_percent_income', 'cb_person_cred_hist_length', 
                       'person_emp_length', 'loan_int_rate']
new_data[numerical_features] = scaler.fit_transform(new_data[numerical_features])

# Display processed input data
st.write("Processed Input Data:")
st.dataframe(new_data)

# Predict button
if st.button("Predict Creditworthiness"):
    # Make prediction
    prediction = model.predict(new_data)
    prediction_prob = model.predict_proba(new_data)[:, 1]

    # Display prediction
    if prediction[0] == 1:
        st.error(f"Prediction: **High Risk** (Probability of default: {prediction_prob[0]:.2f})")
    else:
        st.success(f"Prediction: **Low Risk** (Probability of default: {prediction_prob[0]:.2f})")
