"""
    ALl avaliable platforms for implement social auth
"""

from abc import ABC, abstractmethod
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.exceptions import ValidationError
import requests
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class BaseSocialPlatform(ABC) : 
    
    @abstractmethod
    def get_access_token(self) : ...

    @abstractmethod
    def get_auth_url(self) : ...

    @abstractmethod
    def save_user_data(self) : ...


def generate_tokens_for_user(user) -> dict:
    tokens = RefreshToken.for_user(user)

    return {
        'refresh_token':str(tokens),
        'access_token' : str(tokens.access_token) 
    }

class FacebookAuth(BaseSocialPlatform):
    FB_SOCIAL_AUTH = settings.SOCIAL_AUTH.get('facebook')
    FB_REDIRECT_URL = FB_SOCIAL_AUTH.get('redirect_url')
    FB_CLIENT_ID = FB_SOCIAL_AUTH.get('client_id')
    FB_CLIENT_SECRET = FB_SOCIAL_AUTH.get('client_secret')
    SAVE_USER_DATA_FUNCTION = FB_SOCIAL_AUTH.get('save_user_data')

    def get_access_token(self):...

    def get_auth_url(self):
        url = f"https://www.facebook.com/v14.0/dialog/oauth?client_id={self.FB_CLIENT_ID}&redirect_uri={self.FB_REDIRECT_URL}&scope=email,public_profile,user_friends&response_type=token"
        return url
    
    def get_user_info_by_accessToken(self, access_token) :
        url = f'https://graph.facebook.com/me?access_token={access_token}&fields=id,name,email'
        response = requests.get(url)
        
        if not response.ok :
            raise ValidationError({'error': 'Invalid token.'})
        
        user_info = response.json()
        return user_info
    
    def save_user_data(self, user_dict)  :
        user = self.SAVE_USER_DATA_FUNCTION(user=user_dict)
        return user
    
