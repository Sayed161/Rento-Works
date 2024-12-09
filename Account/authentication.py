from django.contrib.auth.backends import BaseBackend
from .models import User

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Check if the user exists with the provided email
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user  # Return the authenticated user
        except User.DoesNotExist:
            return None