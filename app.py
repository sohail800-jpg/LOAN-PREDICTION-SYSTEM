import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model/loan_model.pkl", "rb"))

st.title("Loan Approval Prediction System")

# Inputs
Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

ApplicantIncome = st.number_input("Applicant Income", min_value=0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)

LoanAmount = st.number_input("Loan Amount", min_value=0)
Loan_Amount_Term = st.number_input("Loan Amount Term", min_value=0)

Credit_History = st.selectbox("Credit History", [1.0, 0.0])

Property_Area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)

# Encoding
Gender = 1 if Gender == "Male" else 0
Married = 1 if Married == "Yes" else 0
Education = 1 if Education == "Graduate" else 0
Self_Employed = 1 if Self_Employed == "Yes" else 0
Credit_History = int(Credit_History)

Dependents_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3
}
Dependents = Dependents_map[Dependents]

Property_Area_map = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}
Property_Area = Property_Area_map[Property_Area]

TotalIncome = ApplicantIncome + CoapplicantIncome

# DataFrame with EXACT features
data = pd.DataFrame([[
    Gender,
    Married,
    Dependents,
    Education,
    Self_Employed,
    ApplicantIncome,
    CoapplicantIncome,
    LoanAmount,
    Loan_Amount_Term,
    Credit_History,
    Property_Area,
    TotalIncome
]], columns=[
    'Gender',
    'Married',
    'Dependents',
    'Education',
    'Self_Employed',
    'ApplicantIncome',
    'CoapplicantIncome',
    'LoanAmount',
    'Loan_Amount_Term',
    'Credit_History',
    'Property_Area',
    'TotalIncome'
])

# Prediction
if st.button("Predict Loan Status"):

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")