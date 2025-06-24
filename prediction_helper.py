# prediction_helper.py
from joblib import load
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load model components
model_data = load('artifacts/model_data.joblib')
model = model_data['model']
scaler = model_data['scaler']
features = model_data['features']
cols_to_scale = model_data['cols_to_scale']

# Define request schema
class CreditRequest(BaseModel):
    age: int
    income: float
    loan_amount: float
    loan_tenure_months: int
    avg_dpd_per_delinquency: float
    delinquency_ratio: float
    credit_utilization_ratio: float
    num_open_accounts: int
    residence_type: str
    loan_purpose: str
    loan_type: str

# Prepare input features
def prepare_input(data: CreditRequest):
    input_data = {
        'age': data.age,
        'loan_tenure_months': data.loan_tenure_months,
        'number_of_open_accounts': data.num_open_accounts,
        'credit_utilization_ratio': data.credit_utilization_ratio,
        'loan_to_income': data.loan_amount / data.income if data.income > 0 else 0,
        'delinquency_ratio': data.delinquency_ratio,
        'avg_dpd_per_delinquency': data.avg_dpd_per_delinquency,
        'residence_type_Owned': 1 if data.residence_type == 'Owned' else 0,
        'residence_type_Rented': 1 if data.residence_type == 'Rented' else 0,
        'loan_purpose_Education': 1 if data.loan_purpose == 'Education' else 0,
        'loan_purpose_Home': 1 if data.loan_purpose == 'Home' else 0,
        'loan_purpose_Personal': 1 if data.loan_purpose == 'Personal' else 0,
        'loan_type_Unsecured': 1 if data.loan_type == 'Unsecured' else 0,
        # Dummy placeholders
        'number_of_dependants': 1,
        'years_at_current_address': 1,
        'zipcode': 1,
        'sanction_amount': 1,
        'processing_fee': 1,
        'gst': 1,
        'net_disbursement': 1,
        'principal_outstanding': 1,
        'bank_balance_at_application': 1,
        'number_of_closed_accounts': 1,
        'enquiry_count': 1
    }

    df = pd.DataFrame([input_data])
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df = df[features]
    return df

# Compute score and rating
def calculate_credit_score(input_df, base_score=300, scale_length=600):
    x = np.dot(input_df.values, model.coef_.T) + model.intercept_
    default_prob = 1 / (1 + np.exp(-x))
    non_default_prob = 1 - default_prob
    credit_score = base_score + non_default_prob.flatten() * scale_length

    def get_rating(score):
        if 300 <= score < 500:
            return 'Poor'
        elif 500 <= score < 650:
            return 'Average'
        elif 650 <= score < 750:
            return 'Good'
        elif 750 <= score <= 900:
            return 'Excellent'
        else:
            return 'Undefined'

    return default_prob.flatten()[0], int(credit_score[0]), get_rating(credit_score[0])

@app.post("/predict")
def predict(data: CreditRequest):
    input_df = prepare_input(data)
    prob, score, rating = calculate_credit_score(input_df)
    return {
        "default_probability": round(prob, 4),
        "credit_score": score,
        "rating": rating
    }
