from django.contrib.auth.backends import BaseBackend
from .models import User
from .jwt_token import verify_jwt_token

class IntraAuthenticationBackend(BaseBackend):
    def authenticate(self, request, jwt_token=None):
        if jwt_token:
            user = verify_jwt_token(jwt_token)
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id42=user_id)
        except User.DoesNotExist:
            return None