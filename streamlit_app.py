import streamlit as st
import webbrowser

st.title("🔗 Open een link direct")

# Inputveld voor de URL
url = st.text_input("Voer een URL in (bijv. https://www.google.com)")

# Knop om de link te openen
if st.button("Open Link"):
    if url:
        js = f"window.open('{url}')"  # JavaScript om de link te openen
        st.markdown(f'<script>{js}</script>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Voer eerst een geldige URL in!")
