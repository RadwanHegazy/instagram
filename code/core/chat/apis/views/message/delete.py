from rest_framework.generics import DestroyAPIView
from chat.models import Message
from globals.permissions import IsMessageSender


class DeleteMessageAPI (DestroyAPIView) :
    permission_classes = [IsMessageSender]
    lookup_field = 'id'

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)
    