from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///MiTiendaCom.db')

Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()