from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import EmailAddress

class Controller:
    def __init__(self):
        self.engine = create_engine("sqlite:///email.sqlite", echo=True)

    def save(self, email, password):
        """
        Save the email
        :param email:
        :param password:
        :return:
        """
        try:

            with Session(self.engine) as sess:
                sess.add(EmailAddress(email=email, password=password))
                sess.commit()
            return f"{email} and password saved!"

        except ValueError as error:
            # show an error message
            raise ValueError(error)


