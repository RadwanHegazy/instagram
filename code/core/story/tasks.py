from celery import shared_task
from .models import Story
from django.utils.timezone import datetime

@shared_task
def story_builder(**controls) : 
    print("Story Builder starts ...")


@shared_task
def check_or_delete_story(*args, **kwargs) : 
    print("Going to check it")
    stories = Story.objects.all()
    for story in stories:
        if datetime.now().timestamp() > story.expired_at.timestamp():
            print('delete story : ', story)
            story.delete()
    print("finish scanning")