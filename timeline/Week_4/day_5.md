# Day 5

Today I work in creating serializers and endpoints for story app, and i createing two serializers :

1. serializer for retrive story 
2. serialzier for create story

Then i create three endpoints : 

1. endpoint for get all your followings stories
2. endpoint for get story by id
3. endpoint for create story

After that i created new container for celery beat, and create celery beat task to run every 1 hr to delete the stories which its time expired.

Unti now i have 2 containers for celery :

1. container for celery worker
2. container for celery beat

This is all about today.