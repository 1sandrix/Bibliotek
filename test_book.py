
import unittest
from book import Book

class TestBook(unittest.TestCase):

    def test_book(self):
        book = Book("Harry Potter", 1)

        self.assertEqual(book.title, "Harry Potter")
        self.assertEqual(book.book_id, 1)

    def test_annan_bok(self):
        book = Book("Sagan om ringen", 2)

        self.assertEqual(book.title, "Sagan om ringen")
        self.assertEqual(book.book_id, 2)


if __name__ == "__main__":
    unittest.main()
