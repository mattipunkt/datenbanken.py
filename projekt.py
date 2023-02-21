# -*- coding: utf-8 -*-
import os, sys, sqlite3
import lib.functions as func
import logging                      # Zum Loggen
from pathlib import Path            # zum erstellen der Datenbank
import time

# Logger zur Detaillierten Aufzeichnung, in Vorbereitung auf die einfachere Verwendung des GUIs, vielleicht später py2exe um eine einfache exe-Datei für Windows bereit zustellen.
logging.basicConfig(filename="dblog %s.log" %time.time(),
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Als erstes überprüfen, ob eine genannte Datenbank bereits existiert
logger.warning("Versuche Datenbank zu erstellen")
if os.path.exists("filme.db"):
    print("Datei bereits vorhanden")
    logger.warning("Datei konnte nicht erstellt werden, da bereits vorhanden")
    sys.exit(0)

logger.info("Verbinde mit der Datenbank")
connection = sqlite3.connect("filme.db")
logger.info("Erfolg! Verbunden mit der DatenbanK")

def datenbankErstellen():
    dbname = input("Name der Datenbank: ")
    print("Der Datenbankname wurde festgelegt auf: ",dbname)
    return


def tabelleErstellen();
    sql = "CREATE TABLE filme(" \
      "titel TEXT, " \
      "vorname TEXT, " \
      "personalnummer INTEGER PRIMARY KEY, " \
      "gehalt REAL, " \
      "geburtstag TEXT)"

print("Wilkommen in deiner persönlichen Filmdatenbank.")
print("Folgende Eingaben sind möglich: ")
print("add      -       Hinzufügen eines Films")

print(time.time())
