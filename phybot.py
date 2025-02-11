import streamlit as st
import google.generativeai as genai

# Configurar API Key de Gemini
genai.configure(api_key="AIzaSyDoxAmNP_00COyHDfBoYTwXGP74_E8tXbc")  # 🔹 Reemplaza con tu clave de Google AI

# Configurar el modelo de IA
modelo = genai.GenerativeModel("gemini-pro")

st.title("Phybot: El assitente virtual de Phymed 🤖")

# Entrada del usuario
user_input = st.text_input("Haz una pregunta sobre equipos médicos:")

# Llamada a Gemini para generar respuesta
if user_input:
    respuesta = modelo.generate_content(user_input)
    st.write(respuesta.text)



