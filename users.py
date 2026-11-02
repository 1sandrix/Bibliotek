import sqlite3
import random
from datetime import datetime, date

def registrera_anvandare():
    fornamn = input("Ange förnamn: ")
    efternamn = input("Ange efternamn: ")
    fodelsedatum = input("Ange födelsedatum (ÅÅÅÅ-MM-DD): ")

    print("\nPersonens uppgifter:")
    print("Namn:", fornamn, efternamn)
    print("Födelsedatum:", fodelsedatum)

    fodd = datetime.strptime(fodelsedatum, "%Y-%m-%d").date()

    idag = date.today()

    alder = idag.year - fodd.year

    if (idag.month, idag.day) < (fodd.month, fodd.day):
        alder -= 1

    print("Ålder:", alder)

    datum = fodd.strftime("%y%m%d")
    slumpnummer = random.randint(0, 9999)

    personnummer = datum + "-" + f"{slumpnummer:04d}"

    print("Personnummer:", personnummer)

    
    conn = sqlite3.connect("bibliotek.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO Users
    (fornamn, efternamn, fodelsedatum, personnummer, alder)
    VALUES (?, ?, ?, ?, ?)
    """, (fornamn, efternamn, fodelsedatum, personnummer, alder))

    conn.commit()

    user_id = cursor.lastrowid

    conn.close()

    print("Du är nu registrerad i biblioteket.")

    
    return user_id
