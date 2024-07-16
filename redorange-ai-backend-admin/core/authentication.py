from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from admin_accounts.models import AdminUsers
from admin_accounts.utils import get_user_id_access_token, is_token_blacklisted

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return None

        try:
            token = token.split(' ')[1]
        except IndexError:
            raise AuthenticationFailed('Invalid token header. No credentials provided.')
        
        if is_token_blacklisted(token):
            raise AuthenticationFailed('Token is blacklisted.')

        user_id = get_user_id_access_token(token)
        if not user_id:
            raise AuthenticationFailed('Invalid token or expired token.')

        try:
            user = AdminUsers.objects.get(id=user_id)
        except AdminUsers.DoesNotExist:
            raise AuthenticationFailed('User not found.')

        return (user, None)
