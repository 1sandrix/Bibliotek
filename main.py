
from book import Book
from users import registrera_anvandare

books = [
    Book("Harry Potter", 1),
    Book("Sagan om ringen", 2),
    Book("Flugornas herre", 3),
    Book("Frankenstein", 4),
    Book("Bröderna Lejonhjärta", 5)
]

print("Bibliotekets böcker:")

for book in books:
    print(book.book_id, book.title)

registrera_anvandare()
