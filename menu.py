from booking import BookingManager
from library import Library
from member import MemberManager


class Menu:
    def __init__(self):
        self.library = Library()
        self.members = MemberManager()
        self.bookings = BookingManager()

    def run(self):
        while True:
            self.show_main_menu()

            choice = input("Enter your choice: ").strip()

            try:
                if choice == "1":
                    self.book_menu()

                elif choice == "2":
                    self.member_menu()

                elif choice == "3":
                    self.borrow_book()

                elif choice == "4":
                    self.return_book()

                elif choice == "5":
                    self.show_borrowed_books()

                elif choice == "6":
                    print("\nGoodbye!")
                    break

                else:
                    print("Invalid choice.")

            except ValueError as error:
                print(f"\nError: {error}")

    @staticmethod
    def show_main_menu():
        print(
            """
==============================
   LIBRARY MANAGEMENT SYSTEM
==============================

1. Book Management
2. Member Management
3. Borrow Book
4. Return Book
5. Borrowed Books
6. Exit
"""
        )

    def book_menu(self):
        while True:
            print(
                """
------- BOOK MANAGEMENT -------

1. Add Book
2. Remove Book
3. Update Book
4. Search by Title
5. Search by Author
6. Display All Books
7. Back
"""
            )

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.remove_book()

            elif choice == "3":
                self.update_book()

            elif choice == "4":
                self.search_title()

            elif choice == "5":
                self.search_author()

            elif choice == "6":
                self.display_books()

            elif choice == "7":
                break

            else:
                print("Invalid choice.")

    def add_book(self):
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        genre = input("What is your book Genre: ")

        book = self.library.add_book( title, author, genre,)

        print(f'Book "{book.title}" added successfully.')

    def remove_book(self):
        book_id = self.get_integer("Book ID: ")

        book = self.library.remove_book(book_id)

        print(
            f'Book "{book.title}" removed successfully.'
        )

    def update_book(self):
        book_id = self.get_integer("Book ID: ")

        title = input("Enter New title: ")
        author = input("Enter New author: ")
        genre = input("Enter New genre: ")

        book = self.library.update_book(
            book_id,
            title,
            author,
            genre,
        )

        print(
            f'Book "{book.title}" updated successfully.'
        )

    def search_title(self):
        title = input("Enter title: ")

        books = self.library.search_by_title(title)

        self.display_book_list(books)

    def search_author(self) -> None:
        author = input("Enter author: ")

        books = self.library.search_by_author(author)

        self.display_book_list(books)

    def display_books(self) :
        books = self.library.get_all_books()

        self.display_book_list(books)

    @staticmethod
    def display_book_list(books):
        if not books:
            print("No books found.")
            return

        print("\nBooks:")

        for book in books:
            print(
                f"[{book.book_id}] "
                f"{book.title} | "
                f"{book.author} | "
                f"{book.genre}"
            )

    def member_menu(self):
        while True:
            print(
                """
------- MEMBER MANAGEMENT -------

1. Register Member
2. View Member
3. Delete Member
4. Display All Members
5. Back
"""
            )

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.register_member()

            elif choice == "2":
                self.view_member()

            elif choice == "3":
                self.delete_member()

            elif choice == "4":
                self.display_members()

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

    def register_member(self) :
        name = input(" Your Name: ")
        email = input("Your Email: ")

        member = self.members.register_member(
            name,
            email,
        )

        print(
            f"Member registered successfully."
            f" Your ID: {member.member_id}"
        )

    def view_member(self):
        member_id = self.get_integer("Member ID: ")

        member = self.members.get_member(member_id)

        print(
            f"\nName: {member.name}\n"
            f"Email: {member.email}\n"
            f"ID: {member.member_id}"
        )

    def delete_member(self):
        member_id = self.get_integer("Member ID: ")

        member = self.members.delete_member(member_id)

        print(
            f"Member '{member.name}' deleted successfully."
        )

    def display_members(self):
        members = self.members.get_all_members()

        if not members:
            print("No members found.")
            return

        for member in members:
            print(
                f"[{member.member_id}] "
                f"{member.name} | {member.email}"
            )

    def borrow_book(self):
        member_id = self.get_integer("Member ID: ")
        book_id = self.get_integer("Book ID: ")
        days = self.get_integer("Borrowing days: ")

        self.members.get_member(member_id)
        self.library.get_book(book_id)

        booking = self.bookings.borrow_book(
            book_id,
            member_id,
            days,
        )

        print(
            f"Book borrowed successfully."
            f" Booking ID: {booking.booking_id}"
        )

    def return_book(self):
        book_id = self.get_integer("Book ID: ")

        booking = self.bookings.return_book(book_id)

        print(
            f"Book returned successfully."
            f" Booking ID: {booking.booking_id}"
        )

    def show_borrowed_books(self):
        bookings = self.bookings.get_active_bookings()

        if not bookings:
            print("No books are currently borrowed.")
            return

        for booking in bookings:
            book = self.library.get_book(booking.book_id)

            print(
                f"\nBook: {book.title}"
                f"\nMember ID: {booking.member_id}"
                f"\nDue: {booking.due_date}"
            )

    @staticmethod
    def get_integer(message: str) -> int:
        value = input(message).strip()

        try:
            return int(value)
        except ValueError:
            raise ValueError(
                "Please enter a valid number."
            )