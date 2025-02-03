from rest_framework import serializers
from ..models import Chat, Message
from users.apis.serializres import UserSerializer


class ChatListSerializer (serializers.ModelSerializer) :

    class Meta:
        model = Chat
        fields = [
            'id',
            'last_msg',
            'last_sender'
        ]

    def to_representation(self, instance:Chat):
        response =  super().to_representation(instance)
        user = self.context.get('user')
        reciver = instance.get_reciver(user)
        response['reciver'] = UserSerializer(reciver).data

        if instance.last_sender:
            response['last_sender'] = UserSerializer(instance.last_sender).data
        return response
    
class GetMessageSerializer (serializers.ModelSerializer) : 
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = [
            'content',
            'sent_at',
            'sender',
            'image'
        ]

