from rest_framework.generics import CreateAPIView
from ..serializers import CreatePostSerializer
from rest_framework.permissions import IsAuthenticated

class CreatePostView (CreateAPIView) : 
    serializer_class = CreatePostSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'owner' : self.request.user,
            'images' : self.request.FILES
        }