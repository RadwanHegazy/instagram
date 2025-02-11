from abc import ABCMeta, abstractmethod

class BaseNotification (metaclass=ABCMeta) : 
    """
    Description :
        Base Notification class for sending notifications.
    
    Params : 
        - sender : User whos send the notification
        - reciver : User whos recive the notification
    
    Methods : 
        - send (Abstracted)
    """

    def __init__(self, sender, reciver):
        self.sender = sender
        self.reciver = reciver

    @abstractmethod
    def send(self) : ...


class LikePostNotification (BaseNotification) : 

    def send(self):
        print(f"sending like post from {self.sender.username} to {self.reciver.username}")


class FollowNotification (BaseNotification) : 
    
    def send(self):
        print(f"{self.sender} Starts to follow {self.reciver}  !")


def send_notification(notification : BaseNotification) :
    notification.send()

