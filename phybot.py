import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore

# Configurar Firebase
cred = credentials.Certificate("TU_ARCHIVO_JSON.json")  # 🔹 Reemplázalo con tu archivo JSON
firebase_admin.initialize_app(cred)
db = firestore.client()

# Configurar API Key de Gemini
genai.configure(api_key="TU_CLAVE_GEMINI")  # 🔹 Reemplázala con tu API Key de Google AI

# Configurar el modelo de IA
modelo = genai.GenerativeModel("gemini-pro")

st.title("Chatbot de Equipos Médicos 🤖")

# Entrada del usuario
user_input = st.text_input("Haz una pregunta sobre equipos médicos:")

# Llamada a Gemini y guardado en Firebase
if user_input:
    respuesta = modelo.generate_content(user_input)
    respuesta_texto = respuesta.text

    # Guardar en Firebase
    doc_ref = db.collection("chat_history").add({
        "pregunta": user_input,
        "respuesta": respuesta_texto
    })

    st.write(respuesta_texto)



