from rest_framework.generics import DestroyAPIView
from notifications.models import Notification
from globals.permissions import IsNotificationReciver

class DeleteNotificationsAPI (DestroyAPIView) : 
    permission_classes = [IsNotificationReciver]
    lookup_field = 'id'
    
    def get_queryset(self):
        return Notification.objects.filter(reciver=self.request.user)