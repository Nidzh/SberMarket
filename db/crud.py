from sqlalchemy.orm import Session
from db.database import get_session


def create(model, payload, refresh=None):
    db: Session = get_session()
    with db:
        db_item = model(**payload)
        db.add(db_item)
        db.commit()
        if refresh:
            db.refresh(db_item)
        return db_item