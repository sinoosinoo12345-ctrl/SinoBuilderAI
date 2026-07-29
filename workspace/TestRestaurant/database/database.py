
from sqlalchemy import create_engine


DATABASE_URL = (
    "sqlite:///restaurant.db"
)


engine = create_engine(
    DATABASE_URL
)
