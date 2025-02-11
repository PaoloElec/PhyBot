
import openai

openai.api_key = "TU_CLAVE_AQUI"  # Reemplaza con tu clave real

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hola, ¿cómo estás?"}]
)

print(response["choices"][0]["message"]["content"])

