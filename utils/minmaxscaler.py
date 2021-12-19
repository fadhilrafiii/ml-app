import streamlit as st
from constants.label import label

def min_max_scaler(col_names, val):
  max = {
    "CNT_CHILDREN":               19.0,
    "AMT_INCOME_TOTAL":    117000000.0,
    "AMT_CREDIT":            4050000.0,
    "AMT_ANNUITY":            258025.5,
    "AMT_GOODS_PRICE":       4050000.0
  }

  min = {
    "CNT_CHILDREN":            0.0,
    "AMT_INCOME_TOTAL":    25650.0,
    "AMT_CREDIT":          45000.0,
    "AMT_ANNUITY":          1615.5,
    "AMT_GOODS_PRICE":     40500.0
  }

  try:
    if (val == ''):
      raise ValueError(f'Value for "{label[col_names]}" is not valid!') 

    # if (int(val) > max[col_names]):
    #   return 1
    # if (int(val) < min[col_names]):
    #   return 0
    
    return (float(val) - min[col_names]) / (max[col_names] - min[col_names])
  except ValueError as err:
    print(repr(err))
    st.warning(str(err))

