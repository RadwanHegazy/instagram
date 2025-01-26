from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..serializers import (
    Post,
    PostsSerializer
)
from rest_framework.permissions import IsAuthenticated

class PostListsView (ListAPIView) :
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        [NOTE] make the query set :
        1. get from cache
        2. Must return all user followings posts -> latest -> must likes
        3. paginate data
        """

        return Post.objects.all()
    

class RetrivePostView (RetrieveAPIView) : 
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'