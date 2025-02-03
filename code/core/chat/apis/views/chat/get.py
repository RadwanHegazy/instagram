from rest_framework.generics import ListAPIView
from ...serializers import Chat, ChatListSerializer
from rest_framework.permissions import IsAuthenticated


class ChatListView (ListAPIView) : 
    serializer_class = ChatListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Chat.objects.filter(users__in=[self.request.user])

    def get_serializer_context(self):
        return {
            'user' : self.request.user
        }
