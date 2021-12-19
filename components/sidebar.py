# Import Packages
import streamlit as st

# Import Constants
from constants.menu import menu

def sidebar():
  col1, col2, col3 = st.sidebar.columns([1,5,1])
  with col2:
    col2.image('public/images/home-credit.jpg', width=200, use_column_width=True)
 
  st.sidebar.title('')
  st.sidebar.title('Menu')
  selected_menu = st.sidebar.selectbox('Choose Menu', menu)
  st.sidebar.text('')
  # st.sidebar.title('Options')
  # checkboxes = [st.sidebar.checkbox(cb, key=cb) for cb in checkbox_sidebar]

  return selected_menu
