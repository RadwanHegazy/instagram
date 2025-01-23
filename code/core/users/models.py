from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User (AbstractUser) :

    first_name = None
    last_name = None
    user_permissions = None
    groups = None

    full_name = models.CharField(max_length=225)
    phonenumber = PhoneNumberField()

    picture = models.ImageField(upload_to='user-pics/',null=True, default='user.png') 
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    followers = models.ManyToManyField('users.User', related_name='user_followers', blank=True)
    followings = models.ManyToManyField('users.User', related_name='user_followings', blank=True)


    def __str__(self):
        return self.full_name
