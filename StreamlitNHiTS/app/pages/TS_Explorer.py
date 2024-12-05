import streamlit as st
import pandas as pd

data = st.session_state.data

col1, col2 = st.columns(2)

with col1:
    st.write('Summary Statistics')
    # Time series group summary - descriptive statistics of each time series in dataset
    st.dataframe(data.describe())

with col2:
    pass

#TODO
# Split to two columns?
# Time Series Description
# All plots are per time series
# Time plot
# Seasonality plot - Box plots over different periods
# Anomaly Plot -Outliers
# ACF plot - shows one time series at a time