from django.urls import path
from .views import login, register, profile
from social_auth.social_views.Facebook import facebook

urlpatterns = [
    path('auth/login/', login.LoginView.as_view(), name='login'),
    path('auth/register/', register.RegisterView.as_view(), name='register'),
    path('profile/', profile.ProfileView.as_view(), name='profile'),
    path('fb/url/',facebook.CreateFacebookAuthLinkView.as_view(), name='fb_login_url'),
    path('fb/auth/',facebook.FacebookAuthView.as_view(), name='fb_login_auth'),
]