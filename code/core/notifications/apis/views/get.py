from rest_framework.generics import ListAPIView
from ..serializers import GetNotificationSerializer
from notifications.models import Notification
from rest_framework.permissions import IsAuthenticated


class ListNotificationsAPI (ListAPIView) : 
    serializer_class = GetNotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(reciver=self.request.user)