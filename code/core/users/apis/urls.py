from django.urls import path
from .views import login, register, profile

urlpatterns = [
    path('auth/login/', login.LoginView.as_view(), name='login'),
    path('auth/register/', register.RegisterView.as_view(), name='register'),
    path('profile/', profile.ProfileView.as_view(), name='profile'),

]