from sqlalchemy import create_engine
from model import Base

engine = create_engine('sqlite:///email.sqlite', echo=True)
Base.metadata.create_all(engine)