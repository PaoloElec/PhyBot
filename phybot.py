import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore

# Verificar si Firebase ya fue inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate("phybot-8bba6-firebase-adminsdk-fbsvc-cabdc938e6.json")  # Reemplázalo con tu archivo JSON
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Configurar API Key de Gemini
genai.configure(api_key="AIzaSyDoxAmNP_00COyHDfBoYTwXGP74_E8tXbc")  # Reemplázala con tu API Key de Google AI

# Configurar el modelo de IA
modelo = genai.GenerativeModel("gemini-pro")

st.title("Chatbot de Equipos Médicos 🤖")

# Entrada del usuario
user_input = st.text_input("Haz una pregunta sobre equipos médicos:")

# Llamada a Gemini y guardado en Firebase
if user_input:
    respuesta = modelo.generate_content(user_input)
    respuesta_texto = respuesta.text

st.write(respuesta_texto)
