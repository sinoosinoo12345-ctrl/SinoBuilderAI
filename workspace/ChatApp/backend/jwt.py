from datetime import datetime, timedelta

from jose import jwt


def create_access_token(
    data,
    expires_minutes,
    secret_key,
    algorithm,
):

    payload = data.copy()

    payload["exp"] = (
        datetime.utcnow()
        + timedelta(
            minutes=expires_minutes
        )
    )

    return jwt.encode(
        payload,
        secret_key,
        algorithm=algorithm,
    )
