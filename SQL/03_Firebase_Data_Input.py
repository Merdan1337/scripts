# Import libraries and set current directory
import firebase_admin
import os

from firebase_admin import credentials
from firebase_admin import firestore
from pathlib import Path

os.chdir(Path(__file__).parent)

# Use a service account
cred = credentials.Certificate("path/serviceAccountKey.json")

# Initialisierung mit priv Schlüssel cred
app = firebase_admin.initialize_app(cred)

# Zugriff auf den Firestore
db = firestore.client()

# Data input
data = {"name":"Merdan", "age": 27, "Geschlecht": "männlich"}
db.collection("people").add(data)
