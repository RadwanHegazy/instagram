from notifications.models import Notification
from rest_framework import serializers
from users.apis.serializres import UserSerializer

class GetNotificationSerializer (serializers.ModelSerializer) : 
    sender = UserSerializer()
    
    class Meta:
        model = Notification
        exclude = ["reciver"]

