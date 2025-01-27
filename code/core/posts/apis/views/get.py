from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..serializers import (
    Post,
    PostsSerializer
)
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from users.models import User

class PostListsView (ListAPIView) :
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        posts = cache.get("posts",None)
        user = self.request.user

        if not posts:
            posts = Post.objects.all()
            cache.set('posts', posts)

        user_timeline = posts.filter(owner__in=user.followings.all()).order_by('-created_at').order_by('likes_by_counter')

        return user_timeline
    

class RetrivePostView (RetrieveAPIView) : 
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class GetUserPosts(ListAPIView) : 
    serializer_class = PostsSerializer
    pagination_class = LimitOffsetPagination
    
    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User,username=username)
        return Post.objects.filter(owner=user)