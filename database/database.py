from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import models


class Database:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

    def add_app(self, data):
        session = self.maker()
        print(1)