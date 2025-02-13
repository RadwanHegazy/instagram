from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from ..serializres import FollowUserSerializer, UnFollowUserSerializer


class BaseFollowUserView (CreateAPIView) : 
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'user' : self.request.user
        }
    

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.status_code = status.HTTP_204_NO_CONTENT
        return response


class FollowUserView (BaseFollowUserView) :
    serializer_class = FollowUserSerializer

class UnFollowUserView (BaseFollowUserView) :
    serializer_class = UnFollowUserSerializer
