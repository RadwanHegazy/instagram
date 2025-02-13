from abc import ABCMeta, abstractmethod
from users.models import User
from notifications.models import Notification

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
        
        Notification.objects.create(
            sender=self.sender,
            reciver=self.reciver,
            content=content
        )
        
class FollowNotification (BaseNotification) : 
    
    def send(self):
        content = f"{self.sender.full_name} starts follow you."
        
        Notification.objects.create(
            sender=self.sender,
            reciver=self.reciver,
            content=content
        )
