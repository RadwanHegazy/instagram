from ..serializers import UpdatePostSerializer, Post
from rest_framework.generics import UpdateAPIView
from globals.permissions import IsPostOwner


class UpdatePostView (UpdateAPIView) : 
    serializer_class = UpdatePostSerializer
    permission_classes = [IsPostOwner]
    lookup_field = 'id'
    queryset = Post.objects.all()