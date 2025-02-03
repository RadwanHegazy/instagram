from django.db import models
from users.models import User
from uuid import uuid4

class Chat (models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    users = models.ManyToManyField(User, related_name='users_chat')
    last_msg = models.CharField(max_length=225, null=True, blank=True)
    last_sender = models.ForeignKey(User, related_name='chat_last_sander', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def get_reciver(self, sender:User) -> User : 
        for user in self.users.all() : 
            if user != sender:
                return user
            
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