
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
conn.close()


def visa_bocker():
    conn = sqlite3.connect("bibliotek.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, title FROM Books
    WHERE id NOT IN (SELECT book_id FROM Loans)
    """)

    books = cursor.fetchall()

    print("Tillgängliga böcker:")

    if not books:
        print("Inga böcker finns tillgängliga.")

    for book in books:
        print(book[0], book[1])

    conn.close()


def lana_bok(user_id):
    visa_bocker()

    try:
        book_id = int(input("\nAnge ID på boken du vill låna: "))
    except ValueError:
        print("Du måste ange ett nummer.")
        return

    conn = sqlite3.connect("bibliotek.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id FROM Books
    WHERE id = ? AND id NOT IN
    (SELECT book_id FROM Loans)
    """, (book_id,))

    book = cursor.fetchone()

    if book:
        cursor.execute("""
        INSERT INTO Loans (book_id, user_id)
        VALUES (?, ?)
        """, (book_id, user_id))

        conn.commit()
        print("Boken  har lånats.")
    else:
        print("Boken är redan utlånad.")

    conn.close()


def mina_lan(user_id):
    conn = sqlite3.connect("bibliotek.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT Books.title
    FROM Loans
    JOIN Books ON Loans.book_id = Books.id
    WHERE Loans.user_id = ?
    """, (user_id,))

    books = cursor.fetchall()

    print("Mina lånade böcker:")

    if not books:
        print("Du har inga lånade böcker.")

    for book in books:
        print(book[0])

    conn.close()


def alla_lan():
    conn = sqlite3.connect("bibliotek.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT Books.title, Users.fornamn, Users.efternamn
    FROM Loans
    JOIN Books ON Loans.book_id = Books.id
    JOIN Users ON Loans.user_id = Users.id
    """)

    loans = cursor.fetchall()

    print("Bibliotekets utlånade böcker:")

    if not loans:
        print("Inga böcker är utlånade.")

    for loan in loans:
        print(loan[0], "- Lånad av:", loan[1], loan[2])

    conn.close()
