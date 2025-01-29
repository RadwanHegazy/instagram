from rest_framework.generics import CreateAPIView
from ..serializers import CreateStorySerializer
from rest_framework.permissions import IsAuthenticated


class CreateStoryView (CreateAPIView) : 
    serializer_class = CreateStorySerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'user' : self.request.user
        }
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.status_code = 204
        return response