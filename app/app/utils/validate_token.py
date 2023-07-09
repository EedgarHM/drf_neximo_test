import jwt
from  django.conf import settings


def validate_token(token):
    try:
        decoded_token = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=['HS256']
        )
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False