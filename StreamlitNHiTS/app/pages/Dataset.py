from typing import Any, Dict, List
import streamlit as st
from utils.load import load_dataset

# Load data
# with st.sidebar.expander("Dataset", expanded=True):
st.title("Dataset")
df_select = st.file_uploader("Upload your own dataset")
option = st.selectbox(
"Or select one from the following:",
("Solar Power", "Australian Electricity Demand", ""),
)
    


st.text_input("Enter a Forecast Horizon", value=26)

# TODO
# # Column names

# # Filtering

# # Resampling

# # Cleaning
