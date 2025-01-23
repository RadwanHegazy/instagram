from rest_framework.generics import CreateAPIView
from ..serializres import LoginSerializer

class LoginView (CreateAPIView) : 
    serializer_class = LoginSerializer
