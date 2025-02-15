from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from ..serializres import FollowUserSerializer, UnFollowUserSerializer
from rest_framework.response import Response


class BaseFollowUserView (CreateAPIView) : 
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'user' : self.request.user
        }
    

    def create(self, request, *args, **kwargs):
        """
        Overrides the default create method to return a 204 No Content response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Handle validation errors
        self.perform_create(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)


class FollowUserView (BaseFollowUserView) :
    serializer_class = FollowUserSerializer

class UnFollowUserView (BaseFollowUserView) :
    serializer_class = UnFollowUserSerializer
