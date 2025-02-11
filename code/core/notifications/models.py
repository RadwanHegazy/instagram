from django.db import models
from users.models import User

class Notification (models.Model) : 
    sender = models.ForeignKey(User, related_name='notification_sender', on_delete=models.CASCADE)
    reciver = models.ForeignKey(User, related_name='notification_reciver', on_delete=models.CASCADE)
    content = models.TextField()
    send_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    

    class Meta:
        ordering = ['-send_at']