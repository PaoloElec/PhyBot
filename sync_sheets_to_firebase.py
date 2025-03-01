import json
import firebase_admin
from firebase_admin import credentials, firestore
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Cargar credenciales de Google Sheets (Asegúrate de subir este archivo JSON a tu repositorio)
GOOGLE_SHEETS_CREDENTIALS_FILE = "requirements/google_sheets_credentials.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# ID de tu Google Sheets (lo encuentras en la URL de tu hoja de cálculo)
SPREADSHEET_ID = "TU_GOOGLE_SHEETS_ID"
RANGE_NAME = "Hoja1!A1:Z1000"  # Ajusta según tu hoja

# Cargar credenciales de Firebase (Asegúrate de subir este archivo JSON a tu repositorio)
FIREBASE_CREDENTIALS_FILE = "requirements/firebase_credentials.json"

# Inicializar Firebase
cred = credentials.Certificate(FIREBASE_CREDENTIALS_FILE)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Conectar a Google Sheets
creds = service_account.Credentials.from_service_account_file(GOOGLE_SHEETS_CREDENTIALS_FILE, scopes=SCOPES)
service = build("sheets", "v4", credentials=creds)

def obtener_datos_sheets():
    """Lee los datos de Google Sheets y los devuelve como una lista de diccionarios."""
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get("values", [])

    if not values:
        print("No se encontraron datos en la hoja de cálculo.")
        return []

    # Convertir la primera fila en claves y el resto en valores
    keys = values[0]  # Encabezados
    data_list = [dict(zip(keys, row)) for row in values[1:]]

    return data_list

def subir_a_firebase(data):
    """Sube los datos obtenidos de Google Sheets a Firebase Firestore."""
    if not data:
        print("No hay datos para subir a Firebase.")
        return
    
    collection_ref = db.collection("equipos_medicos")  # Nombre de la colección en Firestore

    for idx, item in enumerate(data):
        try:
            doc_ref = collection_ref.document(f"equipo_{idx}")  # Crear documento único
            doc_ref.set(item)  # Guardar datos en Firebase
            print(f"Documento equipo_{idx} subido con éxito.")
        except Exception as e:
            print(f"Error al subir equipo_{idx}: {e}")

if __name__ == "__main__":
    datos = obtener_datos_sheets()
    subir_a_firebase(datos)
