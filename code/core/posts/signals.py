from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post
from django.core.cache import cache


@receiver(post_save, sender=Post)
def after_create_new_post(**kwargs) : 
    cache.delete('posts')

    

@receiver(post_delete, sender=Post)
def after_create_new_post(instance, **kwargs) : 
    cache.delete('posts')


