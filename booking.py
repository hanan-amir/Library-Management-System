from datetime import datetime, timedelta

from models import Booking
from storage import JSONStorage


class BookingManager:
    def __init__(self, file_path: str = "data/bookings.json"):
        self.storage = JSONStorage(file_path)
        self.bookings: list[Booking] = []

        self.load_bookings()

    def load_bookings(self) :
        data = self.storage.read()

        self.bookings = [
            Booking.from_dict(booking)
            for booking in data
        ]

    def save_bookings(self):
        data = [
            booking.to_dict()
            for booking in self.bookings
        ]

        self.storage.write(data)

    def _next_id(self):
        if not self.bookings:
            return 1

        return max(
            booking.booking_id
            for booking in self.bookings
        ) + 1

    def borrow_book( self,book_id: int,member_id: int, days: int,):

        if days <= 0:
            raise ValueError(
                "Borrowing days must be greater than zero."
            )

        if self.is_book_borrowed(book_id):
            raise ValueError(
                "This book is already borrowed."
            )

        borrowed_at = datetime.now()
        due_date = borrowed_at + timedelta(days=days)

        booking = Booking(
            booking_id=self._next_id(),
            book_id=book_id,
            member_id=member_id,
            borrowed_at=borrowed_at.isoformat(),
            due_date=due_date.isoformat(),
        )

        self.bookings.append(booking)
        self.save_bookings()

        return booking

    def return_book(self, book_id: int):
        for booking in self.bookings:

            if (
                booking.book_id == book_id
                and booking.returned_at is None
            ):
                booking.returned_at = datetime.now().isoformat()

                self.save_bookings()

                return booking

        raise ValueError(
            "This book is not currently borrowed."
        )

    def is_book_borrowed(self, book_id: int):
        return any(
            booking.book_id == book_id
            and booking.returned_at is None
            for booking in self.bookings
        )

    def get_member_bookings( self, member_id: int,):

        return [
            booking
            for booking in self.bookings
            if booking.member_id == member_id
        ]

    def get_active_bookings(self):
        return [
            booking
            for booking in self.bookings
            if booking.returned_at is None
        ]