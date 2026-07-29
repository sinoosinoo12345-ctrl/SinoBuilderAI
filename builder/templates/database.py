DATABASE_ENGINE = """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_engine(

    settings.DATABASE_URL,

    pool_pre_ping=True,

)

SessionLocal = sessionmaker(

    bind=engine,

    autoflush=False,

    autocommit=False,

)


class Base(DeclarativeBase):

    pass


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
"""
DATABASE_MODELS = """
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from database.engine import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    username = Column(
        String,
        unique=True,
        nullable=False,
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
    )

    password = Column(
        String,
        nullable=False,
    )
"""
CRUD = """
from sqlalchemy.orm import Session


def create_user(
    db: Session,
    user,
):

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def get_user(
    db: Session,
    user_id: int,
):

    return db.query(User).filter(
        User.id == user_id
    ).first()


def get_users(
    db: Session,
):

    return db.query(User).all()
"""
MIGRATION = """
CREATE TABLE users(

id INTEGER PRIMARY KEY,

username TEXT NOT NULL UNIQUE,

email TEXT NOT NULL UNIQUE,

password TEXT NOT NULL

);
"""
SEED = """
from database.session import SessionLocal


def seed():

    db = SessionLocal()

    db.close()


if __name__ == "__main__":

    seed()
"""
DATABASE_TEMPLATE = {

    "engine": DATABASE_ENGINE,

    "models": DATABASE_MODELS,

    "crud": CRUD,

    "migration": MIGRATION,

    "seed": SEED,

}
