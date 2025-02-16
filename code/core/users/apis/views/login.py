from rest_framework.generics import CreateAPIView
from ..serializres import LoginSerializer
from globals.custom_thorttle import LoginThrottle
    
class LoginView (CreateAPIView) : 
    serializer_class = LoginSerializer
    throttle_classes = [LoginThrottle]