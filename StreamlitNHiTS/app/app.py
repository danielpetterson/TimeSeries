import streamlit as st
from utils.load import load_config

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

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

# Initialise session state vars
if 'config' not in st.session_state:
    st.session_state.config = []
if 'instructions' not in st.session_state:
    st.session_state.instructions = []
if 'readme' not in st.session_state:
    st.session_state.readme = []

app.run()