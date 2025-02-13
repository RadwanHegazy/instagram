from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from .apis.serializers import GetNotificationSerializer
from dj_notification.notify import send_notification

@receiver(post_save, sender=Notification)
def send_ws_notification(created, instance : Notification, **kwargs) : 
    if not created:
        return
    
    serializer = GetNotificationSerializer(instance)
    send_notification(
        to_user_id=instance.reciver.id,
        **serializer.data
    )
