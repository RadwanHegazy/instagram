from celery import shared_task
from .models import Story
from django.utils.timezone import datetime
from globals.story_builder import StoryBuilder
from users.models import User
import json

@shared_task
def story_builder(
    user_id,
    text_list,
    image
) :
    
    user = User.objects.get(id=user_id)
    
    st_builder = StoryBuilder(
        text_list,
        image
    )

    story_url = st_builder.build()
    
    story_model = Story.objects.create(
        owner=user,
        url=story_url
    )

    story_model.save()



@shared_task
def check_or_delete_story(*args, **kwargs) : 
    print("Going to check it")
    stories = Story.objects.all()
    for story in stories:
        if datetime.now().timestamp() > story.expired_at.timestamp():
            print('delete story : ', story)
            story.delete()
    print("finish scanning")