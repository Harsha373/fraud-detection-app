import streamlit as st
import joblib
import numpy as np

# Load your saved model
model = joblib.load("model.pkl")  # <- FIXED

st.title("Fraud Detection ML App")

step = st.number_input("Step")
amount = st.number_input("Amount")
oldbalanceOrg = st.number_input("Old Balance Orig")
newbalanceOrig = st.number_input("New Balance Orig")
oldbalanceDest = st.number_input("Old Balance Dest")
newbalanceDest = st.number_input("New Balance Dest")

type_CASH_OUT = st.selectbox("Type CASH_OUT", [0, 1])
type_PAYMENT = st.selectbox("Type PAYMENT", [0, 1])
type_TRANSFER = st.selectbox("Type TRANSFER", [0, 1])

if st.button("Predict"):
    data = np.array([[step, amount, oldbalanceOrg, newbalanceOrig,
                      oldbalanceDest, newbalanceDest,
                      type_CASH_OUT, type_PAYMENT, type_TRANSFER]])
    
    pred = model.predict(data)[0]

    if pred == 1:
        st.error("⚠️ Fraud Detected!")
    else:
        st.success("✔️ Legit Transaction")
