import streamlit as st
import pandas as pd

data = st.session_state.data


st.text_input("Enter a Forecast Horizon", value=26)

st.dataframe(st.session_state.data)