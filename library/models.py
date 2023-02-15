from sqlalchemy import Column, Integer, String, Date, Boolean, Table, UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base, backref
from sqlalchemy.orm import relationship

Base = declarative_base()

book_author = Table("book_author",
                    Base.metadata,
                    Column('book_id', ForeignKey('book.book_id')),
                    Column('author_id', ForeignKey("author.author_id")),
                    UniqueConstraint('book_id', 'author_id')
                    )


book_loan = Table("book_loan",
                  Base.metadata,
                  Column('book_id', ForeignKey('book.book_id')),
                  Column('person_id', ForeignKey("person.person_id")),
                  UniqueConstraint('book_id', 'person_id')
                  )

class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    isbn = Column(String)
    num_pages = Column(Integer)
    publication_date = Column(Date)
    publisher_id = Column(Integer, ForeignKey("publisher.publisher_id"))

    authors = relationship("Author",
                           secondary=book_author,
                           order_by='(Author.author_name)',
                           back_populates="works")

    borrowers = relationship("Person",
                             secondary=book_loan,
                             order_by='(Person.name)',
                             back_populates='on_loan')


    def __repr__(self):
        return f"<Book({self.name})>"


class Publisher(Base):
    __tablename__ = "publisher"
    publisher_id = Column(Integer, primary_key=True, autoincrement=True)
    publisher_name = Column(String)

    def __repr__(self):
        return f"<Publisher({self.name})>"


class Author(Base):
    __tablename__ = "author"
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String)

    works = relationship("Book",
                         secondary=book_author,
                         order_by='(Book.title)',
                         back_populates="authors")

    def __repr__(self):
        return f"<Author({self.name})>"


class Person(Base):
    __tablename__ = "person"
    person_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    membership_expiry = Column(Boolean)

    on_loan = relationship("Book",
                           secondary=book_loan,
                           order_by='(Book.title)',
                           back_populates="borrowers")
    def __repr__(self):
        return f"<Person({self.name})>"



