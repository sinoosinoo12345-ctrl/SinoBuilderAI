from database.session import SessionLocal


def seed():

    db = SessionLocal()

    db.close()


if __name__ == "__main__":

    seed()
