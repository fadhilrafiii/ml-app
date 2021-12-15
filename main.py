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
  selected_menu, checboxes_opt = sidebar()

  if (selected_menu == "My Data"):
    my_data_page()
  elif (selected_menu == "Input Data"):
    input_data_page()
  else:
    prediction_page()