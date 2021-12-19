import streamlit as st

# Import Constant
from constants.radio import yes_no_opt, gender_opt, loan_opt

def prediction_page():
  st.subheader('Credit Repayment Ability Prediction')
  has_car = st.radio('Do you own any car?', yes_no_opt)
  has_realty = st.radio('Do you own any property?', yes_no_opt)
  num_of_children = st.text_input('Number of Children')
  amt_income_total = st.text_input('Total Income')
  amt_credit = st.text_input('Total Credit')
  amt_annuity = st.text_input('Total Annuity')
  amt_goods_price = st.text_input('Total Goods Price')
  loan_type = st.radio('Loan Type', loan_opt)
  gender = st.radio('Gender', gender_opt)

  return ({
    "FLAG_OWN_CAR": [1 if has_car == 'Yes' else 0],
    "FLAG_OWN_REALTY": [1 if has_realty == 'Yes' else 0],
    "CNT_CHILDREN": num_of_children,
    "AMT_INCOME_TOTAL": amt_income_total,
    "AMT_CREDIT": amt_credit,
    "AMT_ANNUITY": amt_annuity,
    "AMT_GOODS_PRICE": amt_goods_price,
    "CASH_LOANS": [1 if loan_type == 'Cash Loan' else 0],
    "REVOLVING_LOANS": [1 if loan_type == 'Revolving Loan' else 0],
    "FEMALE": [1 if gender == 'Female' else 0],
    "MALE": [1 if gender == 'Male' else 0]
  })