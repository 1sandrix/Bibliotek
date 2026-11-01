import unittest
from book import Book

class TestBook(unittest.TestCase):

    def test_book(self):
        book = Book("Harry Potter", 1)

        self.assertEqual(book.title, "Harry Potter")
        self.assertEqual(book.book_id, 1)

if __name__ == "__main__":
    unittest.main()