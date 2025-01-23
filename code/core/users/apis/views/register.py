from rest_framework.generics import CreateAPIView
from ..serializres import RegisterSerializer

class RegisterView (CreateAPIView) : 
    serializer_class = RegisterSerializer
