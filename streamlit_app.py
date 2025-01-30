import streamlit as st

st.title("🔗 Open een link direct")

# Inputveld voor de URL
url = st.text_input("Voer een URL in (bijv. https://www.google.com)")

# JavaScript om de link in een nieuw tabblad te openen
def open_link(new_url):
    st.markdown(f'<script>window.open("{new_url}", "_blank");</script>', unsafe_allow_html=True)

# Knop om de link direct te openen
if st.button("Open Link"):
    if url:
        open_link(url)  # Direct openen in een nieuw tabblad
    else:
        st.warning("⚠️ Voer eerst een geldige URL in!")
