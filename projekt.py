# -*- coding: utf-8 -*-
import os, sqlite3
import logging                      # Zum Loggen
from pathlib import Path            # zum erstellen der Datenbank
import datetime
from prettytable import from_db_cursor

# Logger zur Detaillierten Aufzeichnung, in Vorbereitung auf die einfachere Verwendung des GUIs,
# vielleicht später py2exe um eine einfache exe-Datei für Windows bereit zustellen.
logging.basicConfig(filename="dblog.log",
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

def testtable():    # Zum Test, ob eine Tabelle existiert.
    print('Tabellentest wird gestartet.')
    test = 'SELECT * from filme;'
    cursor.execute(test)
    print('Hier der aktuelle Stand der Datenbank')

    return



def createtable():      # Erstellt eine Tabelle
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
    print("Film soll gelöscht werden!")
    print("Um einen Film zu löschen, musst du den Titel des Films eingeben.")
    deleterequest = input("Titel des Films: ")
    suchesql = 'SELECT * FROM filme WHERE titel LIKE "%{}%"'.format(deleterequest)
    cursor.execute(suchesql)
    print("Folgende Einträge werden gelöscht:")
    output = from_db_cursor(cursor)
    print(output)
    print("Bist du dir sicher, dass du diese Einträge löschen willst?")
    confirm = input("Löschen bestätigen (y/N): ")
    if confirm == "n" or confirm == "N" or confirm == "":
        print("Löschen abgebrochen! Die Datenbank wurde nicht verändert.")
        print("Kehre zum Hauptmenü zurück.")
        main()
    elif confirm == "y" or confirm == "Y":
        deletesql = 'DELETE FROM filme WHERE titel LIKE "%{}%"'.format(deleterequest)
        cursor.execute(deletesql)
        connection.commit()
        connection.close()
        print("Der Film wurde gelöscht!")
        print("Kehre zum Hauptmenü zurück. ")
        main()

# Als erstes überprüfen, ob eine genannte Datenbank bereits existiert
logger.warning("Versuche Datenbank zu erstellen")
print("Versuche die Datenbank zu erstellen...")
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

    sql = 'SELECT titel, schauspieler, laenge, regisseur, bewertung_imdb, verfuegbarkeit, genre FROM filme WHERE "{}" LIKE "%{}%"'.format(search,request)
#    sql = 'SELECT titel, schauspieler, laenge, regisseur, bewertung_imdb, verfuegbarkeit, genre FROM filme'
    cursor.execute(sql)
    mytable = from_db_cursor(cursor)
    print(mytable)
    print("Kehre zum Hauptmenü zurück!")
    main()

def listmovies():
    sql = 'SELECT titel, schauspieler, laenge, regisseur, bewertung_imdb, verfuegbarkeit, genre FROM filme'
    cursor.execute(sql)
    outputtable = from_db_cursor(cursor)
    print(outputtable)
    main()



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
        bewertungip = input("Bewertung (0 bis 10 inkl. Nachkommastellen): ")
        streamingverfeugbarip = input("Verfügbar bei: ")
        genreip = input("Genre: ")
        addmovie(filmip, actorip, laengeip, regisseurip, bewertungip, streamingverfeugbarip, genreip)
    elif selection == "d":
        print("Film löschen!")
        deletemovie()
    elif selection == "l":
        print("Filme anzeigen!")
        listmovies()
    elif selection == "s":
        print("Film suchen!")
        searchmovie()
    else:
        print("Fehler! Falsche Eingabe.")
        main()


logger.info("Verbinde mit der Datenbank")
connection = sqlite3.connect("filme.db")  # Verbinde mit der Datenbank
logger.info("Erfolg! Verbunden mit der DatenbanK")
print("Verbunden mit der Datenbank.")
print("SQLite3 Version: " + sqlite3.version)
cursor = connection.cursor()  # Zum erstellen von Sachen

print('Aktuelle Zeit: {}'.format(datetime.datetime.now()))
print('Wilkommen in der Film-Datenbank!')
logger.info("Starte Datenbank!")
logger.info("SQLite3 Version: " + sqlite3.version)

main()
