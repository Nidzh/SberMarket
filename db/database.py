from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import load_config

config = load_config(".env")
engine = create_engine(f'postgresql://{config.db.user}:{config.db.password}@'
                       f'{config.db.host}/{config.db.database}', echo=True)

get_session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)
