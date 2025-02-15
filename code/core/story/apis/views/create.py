from rest_framework.generics import CreateAPIView
from ..serializers import CreateStorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CreateStoryView (CreateAPIView) : 
    serializer_class = CreateStorySerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'user' : self.request.user,
        }
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Handle validation errors
        self.perform_create(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)
