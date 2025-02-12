from abc import ABCMeta, abstractmethod
from users.models import User
from notifications.models import Notification
from dj_notification.notify import send_notification
from notifications.apis.serializers import GetNotificationSerializer

class BaseNotification (metaclass=ABCMeta) : 
    """
    Description : Base Notification class for sending notifications.
    Params : sender, reciver
    Methods : send() 
    """

    def __init__(self, sender : User, reciver : User):
        self.sender = sender
        self.reciver = reciver

    @abstractmethod
    def send(self) : ...


class LikePostNotification (BaseNotification) : 

    def send(self):
        content = f"{self.sender.full_name} has liked your post !"
        
        # create the notification on the db
        notification = Notification.objects.create(
            sender=self.sender,
            reciver=self.reciver,
            content=content
        )

        notification.save()
        serializer = GetNotificationSerializer(notification)

        # send real-time notification for the user
        send_notification(
            to_user_id=self.reciver.id,
            **serializer.data
        )


class FollowNotification (BaseNotification) : 
    
    def send(self):
        content = f"{self.sender.full_name} starts follow you."
        
        # create the notification on the db
        notification = Notification.objects.create(
            sender=self.sender,
            reciver=self.reciver,
            content=content
        )

        notification.save()
        serializer = GetNotificationSerializer(notification)

        # send real-time notification for the user
        send_notification(
            to_user_id=self.reciver.id,
            **serializer.data
        )
