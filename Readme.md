# Credit Scoring Model: Predicting Creditworthiness

This project involves building a **Credit Scoring Model** that predicts the **creditworthiness** of individuals based on historical financial data. The goal is to create a model that can predict whether a person is likely to default on a loan or not. It is built using machine learning techniques, specifically classification algorithms, to make accurate predictions based on various input features such as age, income, loan amount, and more.

## Project Overview

The **Credit Scoring Model** predicts whether a loan will be **defaulted (1)** or **fully paid (0)** based on an individual's profile. The model was trained using a dataset containing information about loan applicants and their financial status, including:

- **Age, income, home ownership**
- **Loan amount, interest rate, grade**
- **Loan repayment status (target variable)**

### Key Features:
- Predict the probability of a loan default based on applicant details.
- Includes a **Streamlit UI** to allow users to input new applicant data and predict their creditworthiness.
- Handle missing values and categorical features effectively.

## Dataset

The dataset used in this project contains **32,581 rows** and **12 columns**. Here's an overview of the columns:

### Columns:
1. **`person_age`**: Age of the person (integer).
2. **`person_income`**: Annual income of the person (integer).
3. **`person_home_ownership`**: Home ownership status (categorical: `RENT`, `OWN`, `MORTGAGE`, etc.).
4. **`person_emp_length`**: Length of employment (float, with some missing values).
5. **`loan_intent`**: Purpose of the loan (categorical: `PERSONAL`, `EDUCATION`, `MEDICAL`, etc.).
6. **`loan_grade`**: Grade assigned to the loan (categorical).
7. **`loan_amnt`**: Loan amount (integer).
8. **`loan_int_rate`**: Interest rate of the loan (float, with some missing values).
9. **`loan_status`**: Target variable representing loan repayment status (`1` = Defaulted, `0` = Fully paid).
10. **`loan_percent_income`**: Loan amount as a percentage of income (float).
11. **`cb_person_default_on_file`**: Whether the person has defaulted before (categorical: `Y`, `N`).
12. **`cb_person_cred_hist_length`**: Length of credit history (integer).

### Observations:
- Missing values are present in **`person_emp_length`** and **`loan_int_rate`**.
- The target variable is **`loan_status`**, indicating whether a loan was defaulted (`1`) or fully paid (`0`).

## Project Workflow

1. **Data Preprocessing**: 
   - Handle missing values and scale numerical features.
   - Encode categorical features using label encoding.
  
2. **Model Training**: 
   - Train a classification model (e.g., Logistic Regression, Random Forest, etc.) on the preprocessed dataset.
   - Evaluate the model using accuracy, confusion matrix, and other performance metrics.

3. **Saving the Model**:
   - The trained model is saved using **`joblib`** for future predictions.

4. **Streamlit UI**: 
   - A **Streamlit app** was developed to allow users to input applicant details and predict creditworthiness in real-time.

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/credit-scoring-model.git
cd credit-scoring-model
```
### 2. Install Dependencies

Ensure that you have **Python 3.x** installed. You can install the required dependencies using **pip**:

```bash
pip install -r requirements.txt
```
### 3. Run the Streamlit Application
To test the credit scoring model with new data, run the following command:

```bash
streamlit run app.py
```
This will launch a Streamlit web application where you can input details for an applicant and predict whether they will default on the loan.

### 4. Model Prediction

The **Streamlit** app will provide:

- **Creditworthiness Prediction**: Whether the applicant is considered **Low Risk** or **High Risk**.
- **Probability of Default**: The prediction confidence, representing the likelihood of loan default.

## Model Details

The model uses **classification techniques** to predict the likelihood of defaulting on a loan. The following algorithms were considered:

- **Logistic Regression**
- **Random Forest**
- **Gradient Boosting**

The model was evaluated on various performance metrics such as:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**

## Files in the Repository

- **`credit_scoring_model.pkl`**: The saved model after training.
- **`app.py`**: The Streamlit UI script.
- **`credit_risk_dataset.csv`**: The dataset used for model training.
- **`requirements.txt`**: A file containing a list of dependencies for the project.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
