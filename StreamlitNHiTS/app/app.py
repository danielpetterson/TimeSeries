

import streamlit as st
from utils.load import load_config

app = st.navigation([
    st.Page("pages/Introduction.py"),
    st.Page("pages/Dataset.py"), 
    st.Page("pages/Forecast.py"), 
    st.Page("pages/TS_Explorer.py")
    ])

# Load config
config, instructions, readme = load_config(
    "config_streamlit.toml", "config_instructions.toml", "config_readme.toml"
)

app.run()