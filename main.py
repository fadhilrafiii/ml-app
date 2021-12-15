# Import Packages
import streamlit as st

# Import Pages
from pages.input_data import input_data_page
from pages.my_data import my_data_page
from pages.prediction import prediction_page

# Import Components
from components.sidebar import sidebar

page_container = st.container()

with page_container:
  selected_menu = sidebar()

  if (selected_menu == "Input Data"):
    input_data_page()
    col1, col2, col3, col4, col5, col6 = st.columns([7,7,7,7,7,8])
    with col6:
      st.button("Predict Data")
