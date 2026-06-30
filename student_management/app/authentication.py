from django.conf import UserSettingsHolder
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User







class CustomAuthentication(BaseAuthentication):
    def authenticate(self,request):
        username = request.headers.get("username")
        username = 'yuvi'
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")
        return (user,None)


            