import streamlit as st
import webbrowser

st.title("🔗 Open YouTube Direct")

# Knop om direct naar YouTube te gaan
if st.button("Ga naar YouTube"):
    js = "window.open('https://www.youtube.com')"  # JavaScript om een nieuwe tab te openen
    st.markdown(f'<script>{js}</script>', unsafe_allow_html=True)
