import openai
import streamlit as st

# Configura la clave de OpenAI
openai.api_key = "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"

st.title("Chatbot con ChatGPT")

user_input = st.text_input("Dime algo:")
if st.button("Enviar") and user_input:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        answer = response['choices'][0]['message']['content']
        st.text_area("Respuesta", value=answer, height=200)
    except Exception as e:
        st.error(f"Error: {str(e)}")


