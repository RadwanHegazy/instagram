from rest_framework.generics import CreateAPIView
from ..serializers import CreatePostSerializer
from rest_framework.permissions import IsAuthenticated
from ..serializers import LikePostSerializer, RemoveLikePostSerializer
from rest_framework import status

class CreatePostView (CreateAPIView) : 
    serializer_class = CreatePostSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'owner' : self.request.user,
            'images' : self.request.FILES.getlist('images', [])
        }
    


class BaseLovePostView (CreateAPIView) : 
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'user' : self.request.user
        }
    
    def create(self, request, *args, **kwargs):
        respose = super().create(request, *args, **kwargs)
        respose.status_code = status.HTTP_204_NO_CONTENT
        return respose

class LovePostView (BaseLovePostView) : 
    serializer_class = LikePostSerializer

class RemoveLovePostView (BaseLovePostView) : 
    serializer_class = RemoveLikePostSerializer
