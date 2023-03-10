import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from controller import Controller
from model import Base, EmailAddress


class TestModel:
    @pytest.fixture()
    def setup_db(self):
        engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(engine)
        with Session(engine) as sess:
            yield sess

    def test_email(self, setup_db):
        email = EmailAddress(email="ooga@booga.com", password="Passwordy10")
        assert email.email == "ooga@booga.com"

    def test_database(self, setup_db):
        sess = setup_db
        seb = EmailAddress(email="seb@gmail.com", password="Ahiiuh12")
        andy = EmailAddress(email="andrew@hotmail.com", password="iwqdUU90")
        sess.add(seb)
        sess.add(andy)
        sess.commit()
        assert sess.query(EmailAddress).count() == 2
        assert sess.query(EmailAddress)[0].email == "seb@gmail.com"
        assert sess.query(EmailAddress)[1].password == "iwqdUU90"


class TestController:
    @pytest.fixture()
    def setup_controller(self):
        controller = Controller(":memory:")
        Base.metadata.create_all(controller.engine)
        return controller

    def test_save(self, setup_controller):
        controller = setup_controller
        temp_email = "bill@ms.com"
        temp_password = "Billy2023"
        save_message = controller.save(temp_email, temp_password)
        assert save_message == f"{temp_email} and password saved!"

    def test_save_wrong_email(self, setup_controller):
        controller = setup_controller
        with pytest.raises(ValueError) as error:
            controller.save("not_correct", "Correct_password1")
            assert str(error.value) == "Invalid email address"

    def test_save_wrong_password(self, setup_controller):
        controller = setup_controller
        with pytest.raises(ValueError) as error:
            controller.save("correct@ok.com", "bad_password")
            assert str(
                error.value) == "Password must be minimum eight characters, at least one uppercase letter, one lowercase letter and one number"
