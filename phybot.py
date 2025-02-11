import streamlit as st
import openai

# Configurar la API Key (reemplázala con la tuya)
openai.api_key = "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"

st.title("Chatbot de Equipos Médicos 🤖")

# Entrada del usuario
user_input = st.text_input("Haz una pregunta sobre equipos médicos:")

# Llamada a OpenAI para generar respuesta
if user_input:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    st.write(response.choices[0].message.content)


