
import openai

openai.api_key = "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"  # Reemplaza con tu clave real

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hola, ¿cómo estás?"}]
)

print(response["choices"][0]["message"]["content"])

