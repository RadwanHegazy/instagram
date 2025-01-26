from django.db import models
from users.models import User

class PostImage (models.Model) : 
    image = models.ImageField(upload_to='post-imgs/')

    def __str__(self):
        return self.image.url

class Post (models.Model) : 
    owner = models.ForeignKey(User, related_name='user_post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField(null=True, blank=True)
    likes_by = models.ManyToManyField(User, related_name='post_likes_by', blank=True)
    likes_by_counter = models.IntegerField(default=0)
    images = models.ManyToManyField(PostImage, related_name='post_imgs', blank=True)

    def __str__(self):
        return self.owner.username