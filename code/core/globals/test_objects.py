from users.models import User
from rest_framework_simplejwt.tokens import AccessToken


def create_user (
        username = 'test',
        password='test',
        email='test@gmail.com'
):
    user = User.objects.create(username=username, email=email)
    user.set_password(password)
    user.save()
    return user


def create_access_token(user=None) : 
    if not user :
        user = create_user()

    return str(AccessToken.for_user(user))


def create_token_headers(user=None) : 
    if not user:
        user = create_user()
    
    tokens = create_access_token(user)

    return {
        'Authorization' : f"Bearer {tokens}"
    }

    