class Book:
    Total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.Total_books += 1

Book.increment_book_count()
Book.increment_book_count()

print(Book.Total_books)