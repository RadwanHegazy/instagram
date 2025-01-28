from django.db import models
from users.models import User


class Story (models.Model) : 
    owner = models.ForeignKey(User, related_name='user_story', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
    url = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.owner.username
    