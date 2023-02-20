import os, sys, sqlite3
import lib.functions as func
import logging                      # Zum Loggen

# Logger zur Detaillierten Aufzeichnung, in Vorbereitung auf die einfachere Verwendung des GUIs, vielleicht später py2exe um eine einfache exe-Datei für Windows bereit zustellen.
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')


# Als erstes überprüfen, ob eine genannte Datenbank bereits existiert
if os.path.exists("schüler.db"):
    print("Datei bereits vorhanden")
    sys.exit(0)
    
