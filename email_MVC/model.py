from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, validates
import re

Base = declarative_base()

class EmailAddress(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"EmailAddress(email={self.email}, password={self.password})"

    @validates("email")
    def validate_email(self, key, address):
        pattern = r"\b[A-Za-z0-0._%+-]+@[A-Za-z0-0.-]+\.[A-z|a-z]{2,}\b"
        if not re.fullmatch(pattern, address):
            raise ValueError("Invalid email address")
        if key != "email":
            raise ValueError("Key must be \"email\"")
        return address

    @validates("password")
    def validate_email(self, key, address):
        #Eight characters including one uppercase letter, one lowercase letter, and one number or special character.
        pattern = r'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"'
        if not re.fullmatch(pattern, address):
            raise ValueError("Invalid password")
        if key!= "password":
            raise ValueError("Key must be \"password\"")
        return address

