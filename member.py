import random

from models import Member
from storage import JSONStorage


class MemberManager:
    def __init__(self, file_path: str = "data/members.json"):
        self.storage = JSONStorage(file_path)
        self.members: list[Member] = []

        self.load_members()

    def load_members(self):
        data = self.storage.read()
        self.members = [
            Member.from_dict(member)
            for member in data
        ]

    def save_members(self) :
        data = [
            member.to_dict()
            for member in self.members
        ]

        self.storage.write(data)

    def _next_id(self):
        if not self.members:
            return 1001

        return max(member.member_id for member in self.members) + 1

    def register_member(
        self,
        name: str,
        email: str,
    ) -> Member:

        name = name.strip()
        email = email.strip().lower()

        if not name or not email:
            raise ValueError("Name and email are required.")

        if self.find_by_email(email):
            raise ValueError(
                "A member with this email already exists."
            )

        member = Member( member_id=self._next_id(),name=name,email=email,)

        self.members.append(member)
        self.save_members()

        return member

    def find_by_email(self, email: str):
        email = email.strip().lower()

        for member in self.members:
            if member.email == email:
                return member

        return None

    def get_member(self, member_id: int):
        for member in self.members:
            if member.member_id == member_id:
                return member

        raise ValueError("Member not found.")

    def delete_member(self, member_id: int):
        member = self.get_member(member_id)

        self.members.remove(member)
        self.save_members()

        return member

    def get_all_members(self):
        return self.members.copy()