import streamlit as st

st.title("🔗 Open YouTube met een knop")

# Knop om de link te openen
if st.button("Ga naar YouTube"):
    st.markdown(
        '<meta http-equiv="refresh" content="0; url=https://www.youtube.com">',
        unsafe_allow_html=True
    )
