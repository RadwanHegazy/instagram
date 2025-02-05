from rest_framework.generics import ListAPIView
from chat.models import Chat, Message
from ...serializers import GetMessageSerializer
from globals.permissions import InChatUsers, IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

class RetriveChatMessageAPI(ListAPIView) :
    permission_classes = [IsAuthenticated]
    serializer_class = GetMessageSerializer
    lookup_field = 'chat_id'

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        chat = get_object_or_404(Chat,id = chat_id)
        if not InChatUsers().has_object_permission(self.request, self, chat):
            raise PermissionDenied("You don't have permission to access this chat")
        return Message.objects.filter(chat=chat)