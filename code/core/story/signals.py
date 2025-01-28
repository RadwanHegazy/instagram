from django.utils.timezone import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Story

@receiver(post_save, sender=Story)
def set_expired_time(created, instance : Story, **kwargs):
    if not created:
        return
    
    instance.expired_at = instance.created_at + timedelta(hours=24)
    instance.save()
    
