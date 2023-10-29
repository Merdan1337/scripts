# Import libraries
import firebase_admin
import os
import mysql.connector

from firebase_admin import credentials
from firebase_admin import firestore
from pathlib import Path
from mysql.connector import Error


def erstelle_tabelle(db, sql_tbl):
    try:
        cursor = db.cursor()
        cursor.execute(sql_tbl)
        db.commit()
    except:
        print("Tabelle existiert nicht")


db = mysql.connector.connect(
    host="localhost",
    database="neuewoche",
    user="root",
    password="12345"
)



sql_tbl = "CREATE TABLE IF NOT EXISTS 'neuewoche'.'people' ('people_id' INT NOT NULL,\ ON DELETE NO ACTION\ ON UPDATE NO ACTION)\ ENGINE =InnoDB;)"

erstelle_tabelle(db, sql_tbl)