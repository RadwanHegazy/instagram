from django.db import models
from users.models import User
from uuid import uuid4

class Chat (models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    users = models.ManyToManyField(User, related_name='users_chat')
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.id)

class Message (models.Model) :
    chat = models.ForeignKey(Chat, related_name='chat_msg', on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name='msg_sender', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img-content/')

    def __str__(self):
        return self.sender.username