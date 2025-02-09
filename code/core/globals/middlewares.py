from django.http import HttpRequest
from django.contrib.auth.models import AnonymousUser
from users.models import User
from rest_framework_simplejwt.tokens import AccessToken


def JWTAuthenticaton_GraphQL (method) : 
    """
        Custom middleware for only GrapQL endpoints to implement
        JWT authentication and send the user to the method of grapql. 
    """
    def wrapper(self, *args, **kwargs) :
        request = args[0].context
        user = AnonymousUser()
        authorization = None

        headers = request.get('headers', None)

        if headers:
            authorization = headers.get('Authorization', None)
    
        if authorization:
            try : 
                token = authorization.split(' ')[1]
                access_token = AccessToken(token)
                user_id = access_token.payload.get('user_id')
                user = User.objects.get(id=user_id)
            except:
                pass
        

        results = method(self, user, *args, **kwargs)
        return results

    return wrapper