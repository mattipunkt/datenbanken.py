# -*- coding: utf-8 -*-
import os, sqlite3
from beautifultable import BeautifulTable
import logging                      # Zum Loggen
from pathlib import Path            # zum erstellen der Datenbank
import time

# Logger zur Detaillierten Aufzeichnung, in Vorbereitung auf die einfachere Verwendung des GUIs, vielleicht später py2exe um eine einfache exe-Datei für Windows bereit zustellen.
logging.basicConfig(filename="dblog %s.log" %time.time(),
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def pushtodb():
    connection = sqlite3.connect("filme.db")  # Verbinde mit der Datenbank
    connection.commit()
    connection.close()

def datenbankerstellen():
    dbname = input("Name der Datenbank: ")
    print("Der Datenbankname wurde festgelegt auf: ",dbname)
    return

def testtable():
    print('Tabellentest wird gestartet.')
    test = 'SELECT * from filme;'
    cursor.execute(test)
    print('Hier der aktuelle Stand der Datenbank')

    return



def createtable():
        myfile = Path('filme.db')
        myfile.touch(exist_ok=True)
        connection = sqlite3.connect("filme.db")  # Verbinde mit der Datenbank
        cursor = connection.cursor()
        sql = 'CREATE TABLE filme(id INTEGER PRIMARY KEY AUTOINCREMENT, titel TEXT, schauspieler TEXT, laenge INTEGER, regisseur TEXT, bewertung_imdb INTEGER, verfuegbarkeit TEXT, genre TEXT);'
        cursor.execute(sql)
        pushtodb()
        print('Tabelle schon vorhanden')
        return



def addmovie(title, cast, length, director, rating, streaming, genre):
    # sql = 'INSERT INTO filme VALUES(' + name + ', ' + darsteller + ', ' + laenge + ', "' + regisseur + '", ' + rating +
    # ', "' + streaming + '", "' + genre + '")'
    sql = 'INSERT INTO filme(titel, schauspieler, laenge, regisseur, bewertung_imdb, verfuegbarkeit, genre) VALUES ("{}","{}",{},"{}",{},"{}","{}")'.format(title,cast,length,director,rating,streaming,genre)
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Film {} erfolgreich hinzugefügt!".format(title))
    print("Kehre zurück zum Hauptmenü!")
    main()


def deletemovie():
    sql = ''

# Als erstes überprüfen, ob eine genannte Datenbank bereits existiert
logger.warning("Versuche Datenbank zu erstellen")
if os.path.exists("filme.db"):
    print("Datei bereits vorhanden")
    logger.warning("Datei konnte nicht erstellt werden, da bereits vorhanden")
else: 
    createtable()



def searchmovie():
    print("Wonach soll gesucht werden?:")
    print("1 = Titel\n" 
          "2 = Regisseur\n"
          "3 = Schauspieler:in\n"
          "4 = Streaming-Dienst")
    selec = input("Suchauswahl: ")
    if selec == "1":
        search = "titel"
        request = input("Titel eingeben: ")
    elif selec == "2":
        search = "regisseur"
        request = input("Name des Regisseur: ")
    elif selec == "3":
        search = "schauspieler"
        request = input("Name des Schauspielers: ")
    elif selec == "4":
        search = "verfuegbarkeit"
        request = input("Name des Dienstes auswählen: ")
    else:
        print("Fehler! Kehre zum Hauptmenü zurück")
        main()
    sql = 'SELECT * FROM filme WHERE "{}" = "{}"'.format(search,request)
    cursor.execute(sql)
    headers = 'PRAGMA table_info(filme)'
    cursor.execute(headers)
    header = cursor.fetchall
    print(header)
    rows = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_DOTTED)
    table.columns.header = ["name", "rank", "gender"]

    for row in rows:
        print(row)









def main():
    print("Aktionsmöglichkeiten:")
    print("a - Film hinzufügen,   d - Film löschen,    l - Filme anzeigen,     s - Film suchen")
    selection = input("Aktion wählen: ")
    if selection == "a":
        print("Film hinzufügen!")
        filmip = input("Name des Filmes: ")
        actorip = input("Schauspieler: ")
        laengeip = input("Länge: ")
        regisseurip = input("Regisseur: ")
        bewertungip = input("Bewertung (0 bis 10 inkl. Nachkommastellen: ")
        streamingverfeugbarip = input("Verfügbar bei: ")
        genreip = input("Genre: ")
        addmovie(filmip, actorip, laengeip, regisseurip, bewertungip, streamingverfeugbarip, genreip)
    elif selection == "d":
        print("Film löschen!")
        print("TBC")
    elif selection == "l":
        print("Filme anzeigen!")
        print("tbc")
    elif selection == "s":
        print("Film suchen!")
        searchmovie()
    else:
        print("Fehler! Falsche Eingabe.")
        main()


logger.info("Verbinde mit der Datenbank")
connection = sqlite3.connect("filme.db")  # Verbinde mit der Datenbank
logger.info("Erfolg! Verbunden mit der DatenbanK")
print("Verbunden mit der Datenbank")
print("SQLite3 Version: " + sqlite3.version)
cursor = connection.cursor()  # Zum erstellen von Sachen

print('time: {}')
print('Wilkommen in der Film-Datenbank!')
main()


