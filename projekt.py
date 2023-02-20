# -*- coding: utf-8 -*-
import os, sys, sqlite3
import lib.functions as func
import logging                      # Zum Loggen

# Logger zur Detaillierten Aufzeichnung, in Vorbereitung auf die einfachere Verwendung des GUIs, vielleicht später py2exe um eine einfache exe-Datei für Windows bereit zustellen.
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Als erstes überprüfen, ob eine genannte Datenbank bereits existiert
logger.warning("Versuche Datenbank zu erstellen")
if os.path.exists("schueler.db"):
    print("Datei bereits vorhanden")
    logger.warning("Datei konnte nicht erstellt werden, da bereits vorhanden")
    sys.exit(0)

logger.info("Verbinde mit der Datenbank")
connection = sqlite3.connect("schueler.db")
logger.info("Erfolg! Verbunden mit der DatenbanK")
