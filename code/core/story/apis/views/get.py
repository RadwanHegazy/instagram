from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..serializers import Story, GetStorySerializer
from rest_framework.permissions import IsAuthenticated

class ListStoriesView (ListAPIView):
    serializer_class = GetStorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Story.objects.filter(owner__in=self.request.user.followings.all())
    
class RetriveStoryById(RetrieveAPIView) : 
    serializer_class = GetStorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = Story.objects.all()