# main.py
import streamlit as st
import requests

st.title("📊 Credit Risk Modelling")
st.subheader("📝 Applicant & Loan Information")

API_URL = "http://13.55.102.35:8000/predict"

row1 = st.columns(1)
row2 = st.columns(3)
row3 = st.columns(2)
row4 = st.columns(2)
row5 = st.columns(2)
row6 = st.columns(2)

with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row2[0]:
    income = st.number_input('Income', min_value=0, value=1200000)
with row2[1]:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[2]:
    st.text("Loan to Income Ratio:")
    st.text(f"{loan_to_income_ratio:.2f}")

with row3[0]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
with row3[1]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

with row4[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)
with row4[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)

with row5[0]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)
with row5[1]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row6[0]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row6[1]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

if st.button("Calculate risk"):
    input_data = {
        "age": age,
        "income": income,
        "loan_amount": loan_amount,
        "loan_tenure_months": loan_tenure_months,
        "avg_dpd_per_delinquency": avg_dpd_per_delinquency,
        "delinquency_ratio": delinquency_ratio,
        "credit_utilization_ratio": credit_utilization_ratio,
        "num_open_accounts": num_open_accounts,
        "residence_type": residence_type,
        "loan_purpose": loan_purpose,
        "loan_type": loan_type
    }

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            default_probability = result["default_probability"]
            credit_score = result["credit_score"]
            rating = result["rating"]

            st.divider()
            st.subheader("📋 Credit Assessment Summary")
            st.markdown("""
            <style>
            .stProgress > div > div > div > div {
                background-color: #d33c46;
            }
            </style>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="🏆 Credit Rating", value=rating)
            with col2:
                st.metric(label="⭐ Credit Score", value=credit_score)
            with col3:
                st.metric(label="⚠️ Default Probability", value=f"{default_probability:.2%}")

            st.progress(int(default_probability * 100), text="📈 Risk Level")
        else:
            st.error("Failed to get prediction from server.")
    except Exception as e:
        st.error(f"API call failed: {e}")
