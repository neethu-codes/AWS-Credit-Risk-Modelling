import streamlit as st
from prediction_helper import predict

st.title("📊Credit Risk Modelling")

# st.subheader("📝 Applicant Details & Loan Request")
st.subheader("📝 Applicant & Loan Information")

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

# Calculate Loan to Income Ratio and display it
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[2]:
    st.text("Loan to Income Ratio:")
    st.text(f"{loan_to_income_ratio:.2f}")  # Display as a text field
   
# Assign inputs to the remaining controls
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
    default_probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)
    st.divider()
    st.subheader("📋Credit Assessment Summary")
    st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #d33c46;
    }
    </style>
    """, unsafe_allow_html=True)
    # st.metric("Credit Rating", rating)
    # st.write(f"Default Probability: **{default_probability:.2%}**")
    # st.write(f"Credit Score: **{credit_score}**")
    # st.write(f"Rating: **{rating}**")

    credit_rating_help_text = """
    **Credit Rating is determined by the Credit Score:**
    - **Excellent:** 750 - 900
    - **Good:** 650 - 749
    - **Average:** 500 - 649
    - **Poor:** 300 - 499
    - **Undefined:** Scores outside 300-900 range
    """

    col1, col2, col3 = st.columns(3) # Creates three columns

    with col1:

        st.metric(label="🏆Credit Rating", value=rating, help=credit_rating_help_text)

    with col2:
        st.metric(label="⭐Credit Score", value=credit_score) 

    with col3:
        st.metric(label="⚠️Default Probability", value=f"{default_probability:.2%}") 


    st.progress(int(default_probability * 100), text="📈Risk Level") 
   
    st.markdown("---") 