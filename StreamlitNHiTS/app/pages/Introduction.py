import streamlit as st
from utils.load import load_config

# Load config
config, instructions, readme = load_config(
    "config_streamlit.toml", "config_instructions.toml", "config_readme.toml"
)

# Info
st.title("Forecasting with N-HiTS")
st.write(readme["app"]["app_intro"])

st.write("What is NHiTS?")
st.write(readme["app"]["nhits"])