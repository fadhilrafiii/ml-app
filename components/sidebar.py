# Import Packages
import streamlit as st

# Import Constants
from constants.menu import menu
from constants.checkbox_sidebar import checkbox_sidebar

def sidebar():
  st.sidebar.title('Menu')
  selected_menu = st.sidebar.selectbox('Choose Menu', menu)
  st.sidebar.text('')
  st.sidebar.title('Option')
  checkboxes = [st.sidebar.checkbox(cb, key=cb) for cb in checkbox_sidebar]

  return selected_menu, checkboxes
