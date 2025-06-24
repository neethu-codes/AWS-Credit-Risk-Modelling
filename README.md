# Credit-Risk-Modelling

A machine learning-powered **credit risk modeling application** that predicts an individual's **default probability**, computes a standardized **credit score (300–900)**, and assigns a **credit rating** based on financial and demographic data.

Built using `scikit-learn` for modeling and `Streamlit` for the interactive frontend, this app helps financial institutions assess creditworthiness with speed and transparency.


##  Project Overview

The application uses a trained **logistic regression model** to predict the likelihood of credit default. Based on this probability, a credit score is calculated and categorized into qualitative ratings such as *Poor*, *Average*, *Good*, and *Excellent*. The UI allows users to enter data like age, income, loan amount, credit utilization, and more to receive real-time scoring.


##  Features

-  Real-time prediction of **default probability**
-  Calculation of standardized **credit score (300–900 scale)**
-  Assignment of **credit rating** (Poor/Average/Good/Excellent)
-  Clean, intuitive **Streamlit UI**
-  Dynamic computation of derived metrics like **Loan-to-Income Ratio**

##  Dataset Information  

This dataset contains **50,000 loan applicants' records**, including demographic details, financial status, loan details, and credit history. The data is structured with **33 columns**, providing insights into factors influencing credit risk assessment.  

#### **Key Features:**  
- **Customer Information:** `cust_id`, `age`, `gender`, `marital_status`, `employment_status`, `income`, `number_of_dependants`  
- **Residence & Location:** `residence_type`, `years_at_current_address`, `city`, `state`, `zipcode`  
- **Loan Details:** `loan_id`, `loan_purpose`, `loan_type`, `sanction_amount`, `loan_amount`, `processing_fee`, `gst`, `net_disbursement`, `loan_tenure_months`, `principal_outstanding`  
- **Financial Status:** `bank_balance_at_application`, `number_of_open_accounts`, `number_of_closed_accounts`, `credit_utilization_ratio`, `enquiry_count`  
- **Repayment History:** `disbursal_date`, `installment_start_dt`, `total_loan_months`, `delinquent_months`, `total_dpd`  

🔹 **Target Variable:** `default` (boolean) indicates whether a customer defaulted on the loan.  

This dataset is useful for building **credit risk models**, loan approval systems, and financial analytics applications. 

##  Project Setup  
### 1. Clone the Repository  
```bash
git clone https://github.com/neethu-codes/Credit-Risk-Modelling.git
cd Credit-Risk-Modelling
```
### 2. Create and Activate Virtual Environment
```bash
python -m venv venv  
source venv/bin/activate  # On Mac/Linux  
venv\Scripts\activate  # On Windows  
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt 
```
### 4. Run the Streamlit App
```bash
streamlit run main.py
```
## Project Structure
```
credit-risk-modelling/
 
├── main.py # Streamlit application
├── prediction_helper.py # Function to load and run the model
│── artifacts/
│ ├── model.joblib # Pre-trained model 
│── requirements.txt # Dependencies
│── README.md # Project documentation
```
## App Preview
Here’s a preview of the application:

<img src="credit-risk-model-project-screenshot.png" alt="App Screenshot" width="700">