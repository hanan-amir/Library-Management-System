from models import Book
from storage import JSONStorage


class Library:
    def __init__(self, file_path: str = "data/books.json"):
        self.storage = JSONStorage(file_path)
        self.books: list[Book] = []

        self.load_books()

    def load_books(self) -> None:
        data = self.storage.read()
        self.books = [Book.from_dict(book) for book in data]

    def save_books(self) -> None:
        data = [book.to_dict() for book in self.books]
        self.storage.write(data)

    def _next_id(self) -> int:
        if not self.books:
            return 1

        return max(book.book_id for book in self.books) + 1

    def add_book( self,title: str,author: str,genre: str,):

        title = title.strip()
        author = author.strip()
        genre = genre.strip()

        if not title or not author or not genre:
            raise ValueError("All book fields are required.")

        if self.find_by_title(title):
            raise ValueError("A book with this title already exists.")

        book = Book(
            book_id=self._next_id(),
            title=title,
            author=author,
            genre=genre,
        )

        self.books.append(book)
        self.save_books()

        return book

    def remove_book(self, book_id: int):
        book = self.get_book(book_id)

        self.books.remove(book)
        self.save_books()

        return book

    def update_book(self,book_id: int,title: str, author: str ,genre: str ,):

        book = self.get_book(book_id)

        if title is not None and title.strip():
            book.title = title.strip()

        if author is not None and author.strip():
            book.author = author.strip()

        if genre is not None and genre.strip():
            book.genre = genre.strip()

        self.save_books()

        return book

    def get_book(self, book_id: int):
        for book in self.books:
            if book.book_id == book_id:
                return book

        raise ValueError("Book not found.")

    def find_by_title(self, title: str):
        title = title.strip().lower()

        for book in self.books:
            if book.title.lower() == title:
                return book

        return None

    def search_by_title(self, title: str):
        title = title.strip().lower()

        return [
            book
            for book in self.books
            if title in book.title.lower()
        ]

    def search_by_author(self, author: str):
        author = author.strip().lower()

        return [
            book
            for book in self.books
            if author in book.author.lower()
        ]

    def get_all_books(self) -> list[Book]:
        return self.books.copy()