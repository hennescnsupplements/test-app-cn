import streamlit as st
import time

# === UI Styling voor premium look ===
st.markdown("""
    <style>
        .big-title { font-size: 36px; font-weight: bold; color: #ff4b4b; text-align: center; }
        .sub-title { font-size: 20px; color: #666; text-align: center; }
        .stButton>button { background-color: #ff4b4b; color: white; font-size: 18px; padding: 10px 20px; border-radius: 10px; }
        .stTextInput>div>div>input { border-radius: 10px; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

# === Hoofdtitel ===
st.markdown('<p class="big-title">🔥 Lijpe Streamlit UI 🔥</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Interactieve knoppen, inputvelden en meer...</p>', unsafe_allow_html=True)
st.write("---")

# === Sidebar ===
st.sidebar.title("🚀 Quick Actions")
st.sidebar.button("🔄 Refresh")
st.sidebar.checkbox("💡 Dark Mode")
st.sidebar.radio("🌍 Kies een optie:", ["Home", "Over", "Contact"])
st.sidebar.text_input("📧 E-mail:")
st.sidebar.slider("🎚️ Kies een waarde:", 0, 100, 50)
st.sidebar.write("---")
st.sidebar.markdown("**💬 Feedback:**")
st.sidebar.text_area("Geef je mening...")

# === Interactieve layout ===
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔥 Start Game"):
        st.success("Game gestart!")

with col2:
    if st.button("🎵 Play Music"):
        st.info("Muziek afspelen...")

with col3:
    if st.button("💰 Check Balance"):
        st.warning("Saldo niet beschikbaar.")

# === Inputvelden ===
naam = st.text_input("👤 Naam invoeren:")
nummer = st.number_input("🔢 Voer een getal in:", min_value=0, max_value=100, value=50)
keuze = st.selectbox("📌 Kies een optie:", ["Optie 1", "Optie 2", "Optie 3"])

# === Sliders & Progress Bar ===
progress = st.slider("📊 Voortgang:", 0, 100, 25)
progress_bar = st.progress(0)
for percent in range(progress):
    time.sleep(0.01)
    progress_bar.progress(percent + 1)

st.write("---")

# === Laatste interactieve sectie ===
st.markdown("### 🚀 Let's go!")
if st.button("💥 BOOM"):
    st.balloons()

st.markdown("🎉 **Have fun met deze UI!** 🚀🔥")
