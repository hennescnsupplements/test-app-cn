import streamlit as st

st.title("🔗 Open een link")

# Inputveld om een link in te voeren
url = st.text_input("Voer een URL in (bijv. https://www.google.com)")

# Knop om de link te openen
if st.button("Open Link"):
    if url:  # Check of er een link is ingevuld
        st.markdown(f'[Klik hier om de link te openen]({url})', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Voer eerst een geldige URL in!")
