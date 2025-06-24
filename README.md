# 📊 Credit Risk Modelling

A machine learning-powered credit risk modeling application that predicts an individual's **default probability**, computes a standardized **credit score (300–900)**, and assigns a **credit rating** (Poor / Average / Good / Excellent).

Built using **FastAPI** for the backend API, **Streamlit** for the interactive frontend and **scikit-learn** for modeling. The backend is containerized with **Docker** and deployed on **AWS EC2**.


##  Project Overview

This application uses a trained **logistic regression model** to:

- Predict the probability that an applicant will **default** on a loan
- Convert that probability into a **credit score** (scaled between 300–900)
- Assign a **credit rating** based on the score


##  Features

-  Predicts **default probability**
-  Computes **credit score**
-  Assigns **credit rating** (Poor / Average / Good / Excellent)
-  Modular prediction logic with preprocessing
-  **Dockerized FastAPI** backend for easy deployment
-  Deployed and tested on **AWS EC2**
-  Interactive Streamlit UI 


##  Dataset Information  

This dataset contains **50,000 loan applicants' records**, including demographic details, financial status, loan details, and credit history. The data is structured with **33 columns**, providing insights into factors influencing credit risk assessment.  

#### **Key Features:**  
- **Customer Information:** `cust_id`, `age`, `gender`, `marital_status`, `employment_status`, `income`, `number_of_dependants`  
- **Residence & Location:** `residence_type`, `years_at_current_address`, `city`, `state`, `zipcode`  
- **Loan Details:** `loan_id`, `loan_purpose`, `loan_type`, `sanction_amount`, `loan_amount`, `processing_fee`, `gst`, `net_disbursement`, `loan_tenure_months`, `principal_outstanding`  
- **Financial Status:** `bank_balance_at_application`, `number_of_open_accounts`, `number_of_closed_accounts`, `credit_utilization_ratio`, `enquiry_count`  
- **Repayment History:** `disbursal_date`, `installment_start_dt`, `total_loan_months`, `delinquent_months`, `total_dpd`  

🔹 **Target Variable:** `default` (boolean) indicates whether a customer defaulted on the loan.  



##  Project Structure

```
credit-risk-modelling/
├── prediction_helper.py        # ML preprocessing and scoring logic
├── main.py                     # (Optional) Streamlit frontend
├── artifacts/
│   └── model_data.joblib       # Trained model, scaler, and feature info
├── Dockerfile                  # Docker build instructions
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```



##  Project Setup

Choose one of the two options below to get started:



###  Option 1: Run with Docker (Recommended)

1. **Build the Docker image**

```bash
docker build -t msneethu/credit-risk-api .
```

2. **Run the container**

```bash
docker run -p 8000:8000 msneethu/credit-risk-api
```

3. **Access the API**

Open: [http://localhost:8000/docs](http://localhost:8000/docs)




###  Option 2: Run Locally (Without Docker)

1. **Clone the repository**

```bash
git clone https://github.com/neethu-codes/Credit-Risk-Modelling.git
cd Credit-Risk-Modelling
```

2. **Create and activate virtual environment**

```bash
python -m venv venv

# On Mac/Linux
source venv/bin/activate

# On Windows
venv\scripts\Activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the FastAPI app**

```bash
uvicorn prediction_helper:app --reload
```

5. **Open API docs**

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)



###  Run Streamlit Frontend

```bash
streamlit run main.py
```



##  AWS EC2 Deployment

Already deployed successfully using Docker on AWS EC2

### Steps:

1. **Launch EC2 instance**
   - Use Ubuntu 20.04 or Amazon Linux 2
   - Open port **8000** in security group

2. **Install Docker**

```bash
sudo apt update
sudo apt install docker.io -y
```

3. **Pull and run the image**

```bash
docker pull msneethu/credit-risk-api
docker run -d -p 8000:8000 msneethu/credit-risk-api
```

4. **Test the API**

Visit: `http://<EC2-Public-IP>:8000/docs`




##  API Request Example

**POST** `/predict`

```json
{
  "age": 28,
  "income": 1200000,
  "loan_amount": 2560000,
  "loan_tenure_months": 36,
  "avg_dpd_per_delinquency": 20,
  "delinquency_ratio": 30,
  "credit_utilization_ratio": 30,
  "num_open_accounts": 2,
  "residence_type": "Owned",
  "loan_purpose": "Home",
  "loan_type": "Unsecured"
}
```

**Response:**

```json
{
  "default_probability": 0.13,
  "credit_score": 765,
  "rating": "Excellent"
}
```

## App Preview
Here’s a preview of the application:

<img src="credit-risk-model-project-screenshot.png" alt="App Screenshot" width="700">
