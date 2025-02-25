import gspread
import firebase_admin
from firebase_admin import credentials, firestore

# 1️⃣ Inicializar Firebase con las credenciales
if not firebase_admin._apps:
    cred = credentials.Certificate("phybot-8bba6-firebase-adminsdk-fbsvc-cabdc938e6.json")  # Reemplázalo con el JSON de Firebase
    firebase_admin.initialize_app(cred)

db = firestore.client()

# 2️⃣ Conectar con Google Sheets usando las credenciales
gc = gspread.service_account(filename="hip-sight-451618-m2-e216d96431b0.json")  # Reemplázalo con el JSON de Google Sheets
spreadsheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1RGydganymG5apc5PAh4vvQVbFAACZECe/edit?gid=419674014#gid=419674014")  # Reemplázalo con la URL del Google Sheets
sheet = spreadsheet.sheet1

# 3️⃣ Leer los datos de la hoja de cálculo
data = sheet.get_all_records()

# 4️⃣ Subir los datos a Firebase
for row in data:
    db.collection("equipos").add(row)

print("✅ Datos subidos correctamente a Firebase")

