
import sqlite3

conn = sqlite3.connect("bibliotek.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY,
    title TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    fornamn TEXT,
    efternamn TEXT,
    fodelsedatum TEXT,
    personnummer TEXT,
    alder INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Loans (
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (book_id) REFERENCES Books(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
)
""")

conn.commit()



books = [
    (1, "Harry Potter"),
    (2, "Sagan om ringen"),
    (3, "Flugornas herre"),
    (4, "Frankenstein"),
    (5, "Bröderna Lejonhjärta")
]

cursor.executemany("""
INSERT OR IGNORE INTO Books (id, title)
VALUES (?, ?)
""", books)

conn.commit()

print("Böckerna har sparats i databasen.")

conn.close()
