import os
import jwt

def generate_token(user):
    SECRET_KEY = os.environ['SECRET_KEY']
    ALGORITHM = 'HS256'

    payload = {
        'user_id': user.id,
        'email' : user.email
    }

    token = jwt.encode(payload, SECRET_KEY, ALGORITHM)

    return token