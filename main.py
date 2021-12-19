# Import Packages
import streamlit as st
import joblib
import pandas as pd

# Import Pages
from pages.prediction import prediction_page

# Import Components
from components.sidebar import sidebar
from utils.minmaxscaler import min_max_scaler

page_container = st.container()
with page_container:
  selected_menu = sidebar()
  st.title('Home Credit')
  if (selected_menu == "Predict Data"):
    data_input = prediction_page()
    print(data_input)
    # Predict Function
    def predict():
      try:
        data_input["CNT_CHILDREN"] = [min_max_scaler("CNT_CHILDREN", data_input["CNT_CHILDREN"])]
        data_input["AMT_INCOME_TOTAL"] = [min_max_scaler("AMT_INCOME_TOTAL", data_input["AMT_INCOME_TOTAL"])]
        data_input["AMT_CREDIT"] = [min_max_scaler("AMT_CREDIT", data_input["AMT_CREDIT"])]
        data_input["AMT_ANNUITY"] = [min_max_scaler("AMT_ANNUITY", data_input["AMT_ANNUITY"])]
        data_input["AMT_GOODS_PRICE"] = [min_max_scaler("AMT_GOODS_PRICE", data_input["AMT_GOODS_PRICE"])]
        clf = joblib.load('model.pkl')
        data_test = pd.DataFrame(data_input)
        data_pred = clf.predict(data_test)
        print(data_input)
        print(data_pred)
        if (data_pred[0] == 1):
          st.success('You are ELIGIBLE to take the credit')
        else:
          st.error('You are NOT ELIGIBLE to take the credit')
      except Exception as e:
        print(str(e))
        st.warning('Predict failed!')
      # y_pred = clf.predict([data_test])
      # print(y_pred)
    st.button("Predict Data", on_click=predict)
