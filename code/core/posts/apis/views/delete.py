from rest_framework.generics import DestroyAPIView
from ..serializers import Post, PostsSerializer
from globals.permissions import IsPostOwner

class DeletePostView (DestroyAPIView) : 
    serializer_class = PostsSerializer
    permission_classes = [IsPostOwner]
    lookup_field = 'id'
    queryset = Post.objects.all()
