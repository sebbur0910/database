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
    def validate_password(self, key, address):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        if not re.fullmatch(pattern, address):
            raise ValueError("Password must be minimum eight characters, at least one uppercase letter, one lowercase letter and one number")
        if key!= "password":
            raise ValueError("Key must be \"password\"")
        return address

