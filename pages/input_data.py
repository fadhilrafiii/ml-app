# Import Packages
import streamlit as st

# Import Constants
from constants.radio import yes_no_opt, gender_opt



def input_data_page():
  col1, col2, col3 , col4, col5 = st.columns([1,1,1,1,1])
  st.title('Input Data')
  has_car = st.radio('Has Car?', yes_no_opt)
  has_realty = st.radio('Has Property?', yes_no_opt)
  num_of_children = st.text_input('Number of Children')
  amt_income_total = st.text_input('Total Income')
  amt_credit = st.text_input('Total Credit')
  amt_annuity = st.text_input('Total Annuity')
  amt_goods_price = st.text_input('Total Goods Price')
  cash_loans = st.text_input('Cash Loans')
  revolving_loans = st.text_input('Revolving Loans')
  gender = st.radio('Gender', gender_opt)
