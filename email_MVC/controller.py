from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import EmailAddress

class Controller:
    def __init__(self):
        self.engine = create_engine("sqlite:///emails.sqlite", echo=True)

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            with Session(self.engine) as sess:
                sess.add(EmailAddress(email=email))
                sess.commit()
            return f"{email} saved!"

        except ValueError as error:
            # show an error message
            raise ValueError(error)
