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
