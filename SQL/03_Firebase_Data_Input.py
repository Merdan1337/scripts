# Import libraries and set current directory
import firebase_admin
import os

from firebase_admin import credentials
from firebase_admin import firestore
from pathlib import Path

os.chdir(Path(__file__).parent)

# Use a service account
cred = credentials.Certificate("path/serviceAccountKey.json")

# Initialize with private key cred
app = firebase_admin.initialize_app(cred)

# Access to the firestore client
db = firestore.client()

# Data input
data = {"name":"Merdan", "age": 27, "gender": "male"}
db.collection("people").add(data)
