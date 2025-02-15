from rest_framework.generics import CreateAPIView
from ..serializers import CreatePostSerializer
from rest_framework.permissions import IsAuthenticated
from ..serializers import LikePostSerializer, RemoveLikePostSerializer
from rest_framework import status
from rest_framework.response import Response

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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Handle validation errors
        self.perform_create(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LovePostView (BaseLovePostView) : 
    serializer_class = LikePostSerializer

class RemoveLovePostView (BaseLovePostView) : 
    serializer_class = RemoveLikePostSerializer
