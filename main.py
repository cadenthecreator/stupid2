import streamlit as st
import streamlit.components.v1 as components

url = st.text_input("Website")
components.iframe(url, height=500)
