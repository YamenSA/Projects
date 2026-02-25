import streamlit as st

st.set_page_config(page_title="Uni-Skript Chatbot", page_icon="📚")

st.title("📚 Chatte mit deinem Skript")
st.write("Willkommen! Bald kannst du hier PDFs hochladen und befragen.")

# Eine einfache Chat-Eingabe (noch ohne Funktion)
user_input = st.chat_input("Stelle eine Frage zu deinem Skript...")

if user_input:
    st.write(f"Du hast gefragt: **{user_input}**")