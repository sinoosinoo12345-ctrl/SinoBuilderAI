
from sqlalchemy.orm import DeclarativeBase


class Base(
    DeclarativeBase
):
    pass



class Order:

    id: int
    customer: str
    total: float



class Product:

    id: int
    name: str
    price: float
