from celery import shared_task


@shared_task
def story_builder(**controls) : 
    print("Story Builder starts ...")