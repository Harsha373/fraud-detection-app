import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("Fraud Detection ML App")

st.write("Enter transaction details below:")

# Numerical Inputs
step = st.number_input("Step", min_value=0.0)
amount = st.number_input("Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0)

# One-Hot Encoded Transaction Types
type_CASH_OUT = st.selectbox("Type: CASH_OUT", [0, 1])
type_DEBIT = st.selectbox("Type: DEBIT", [0, 1])
type_PAYMENT = st.selectbox("Type: PAYMENT", [0, 1])
type_TRANSFER = st.selectbox("Type: TRANSFER", [0, 1])

# Prepare data in the correct order
input_data = np.array([[ 
    step,
    amount,
    oldbalanceOrg,
    newbalanceOrig,
    oldbalanceDest,
    newbalanceDest,
    type_CASH_OUT,
    type_DEBIT,
    type_PAYMENT,
    type_TRANSFER
]])

if st.button("Predict"):
    pred = model.predict(input_data)[0]

    if pred == 1:
        st.error("⚠️ Fraud Detected!")
    else:
        st.success("✔️ Legit Transaction")
