from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    genre: str

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            book_id=data["book_id"],
            title=data["title"],
            author=data["author"],
            genre=data["genre"],
        )


@dataclass
class Member:
    member_id: int
    name: str
    email: str

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            member_id=data["member_id"],
            name=data["name"],
            email=data["email"],
        )


@dataclass
class Booking:
    booking_id: int
    book_id: int
    member_id: int
    borrowed_at: str
    due_date: str
    returned_at: str
    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "book_id": self.book_id,
            "member_id": self.member_id,
            "borrowed_at": self.borrowed_at,
            "due_date": self.due_date,
            "returned_at": self.returned_at,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            booking_id=data["booking_id"],
            book_id=data["book_id"],
            member_id=data["member_id"],
            borrowed_at=data["borrowed_at"],
            due_date=data["due_date"],
            returned_at=data.get("returned_at"),
        )