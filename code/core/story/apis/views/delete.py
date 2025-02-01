from globals.permissions import IsStoryOwner
from rest_framework.generics import DestroyAPIView
from story.models import Story

class DeleteStoryView (DestroyAPIView) : 
    queryset = Story.objects.all()
    permission_classes = [IsStoryOwner]
    lookup_field = 'id'