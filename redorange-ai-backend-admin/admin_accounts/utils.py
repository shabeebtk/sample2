import jwt
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from .models import AdminUsers, BlacklistedToken


SECRET_KEY = settings.SECRET_KEY

def create_access_token(user):
    payload = {
        'user_id': user.id,
        'email' : user.email,
        'exp': datetime.utcnow() + timedelta(minutes=15),
        'iat': datetime.utcnow(),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def create_refresh_token(user):
    payload = {
        'user_id': user.id,
        'email' : user.email,
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    
def get_user_id_access_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def create_tokens_for_user(user):
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return access_token, refresh_token
    
    
def is_token_blacklisted(token):
    return BlacklistedToken.objects.filter(token=token).exists()

def blacklist_token(token):
    if not is_token_blacklisted(token):
        BlacklistedToken.objects.create(token=token)