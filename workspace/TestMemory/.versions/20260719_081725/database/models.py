
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Payment:

    id: int
    amount: float
