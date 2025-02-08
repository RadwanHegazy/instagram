
import graphene
from .objects import PostType, PostImage
from posts.models import Post
from django.core.cache import cache

class Query(graphene.ObjectType):
    user_timeline = graphene.List(PostType)

    def resolve_user_timeline(self, info, **kwargs):
        user = info.context.user

        if not user.is_authenticated:
            raise Exception("Authentication required")

        posts = cache.get("posts",None)

        if not posts:
            posts = Post.objects.all()
            cache.set('posts', posts)

        return posts.filter(owner__in=user.followings.all()).order_by('-created_at').order_by('likes_by_counter')

posts_schema = graphene.Schema(query=Query)
