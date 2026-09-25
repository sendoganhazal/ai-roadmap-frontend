import streamlit as st
import requests

# BACKEND URL
BACKEND_URL = "https://ai-roadmap-backend-nkdi.onrender.com/roadmap" # Render + endpoint

st.set_page_config(page_title = "AI Yol Haritası", page_icon = "🧠", layout = "centered")
st.title("AI Yol Haritası Uygulaması")
st.write("Bir alan seçin, ai size hazır yol haritası göndersin")

secim = st.selectbox(
    "Alan Seçin",
    ["yapay_zeka", "derin_ogrenme", "nlp"]
)

if st.button("Yol haritası getir"):

    try:
        response = requests.post(BACKEND_URL, json = {"alan": secim}, timeout=50)

        data = response.json()

        if "error" in data:
            st.error(data["error"])
        else:
            st.success(f"Seçilen alan: {data['alan']}")
            st.subheader("Yol haritası")
            for i, adim in enumerate(data["adimlar"], start  = 1):
                st.write(f"{i}. {adim}")

    except Exception as e:
        st.error(f"Baglanti hatasi: {e}")