import streamlit as st
from my_component import my_component

st.title("Streamlit Popup Example")

my_component("Name From Streamlit", key="foo")