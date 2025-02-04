from rest_framework.generics import ListAPIView
from chat.models import Chat, Message
from ...serializers import GetMessageSerializer
from globals.permissions import InChatUsers
from django.shortcuts import get_object_or_404

class RetriveChatMessageAPI(ListAPIView) :
    permission_classes = [InChatUsers]
    serializer_class = GetMessageSerializer
    lookup_field = 'chat_id'

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        chat = get_object_or_404(Chat,id = chat_id)
        return Message.objects.filter(chat=chat)