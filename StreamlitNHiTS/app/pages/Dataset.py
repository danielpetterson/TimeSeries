from typing import Any, Dict, List
import streamlit as st
from utils.load import load_dataset
import pandas as pd

#Testing
from statsmodels import datasets

if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame()
if 'updated_data' not in st.session_state:
    st.session_state.updated_data = pd.DataFrame()

# Load data
st.title('Dataset Viewer')
df_select = st.file_uploader('Upload your own dataset (CSV format)')

options = st.selectbox(
'Or select one from the following:',
('', 'Solar Power', 'Australian Electricity Demand'),
)
#--------------------------------
# Testing
data = datasets.elnino.load_pandas().data 
st.session_state.data = data
# Display the dataset
st.subheader('Dataset')
st.dataframe(st.session_state.data)
#--------------------------------

if options != '':
   df_select = options
elif df_select is not None:
 data = pd.read_csv(df_select)
 st.session_state.data = data
 # Display the dataset
 st.subheader('Dataset')
 st.dataframe(st.session_state.updated_data)



# TODO
# Formatting
# Convert temporal variable to datetime and try to convert others to numeric
# Need to have user define datetime format

# Filtering
# Select which is datetime and which are the series of interest (numeric)
# Checkbox or multiselect box

# Resampling
# Remove sections e.g. weekends/holidays

# Cleaning
# Check for missing values
# If found, option to imput or inform user

# Save after cleaning
