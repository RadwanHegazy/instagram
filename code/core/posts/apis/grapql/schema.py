
import graphene
from .objects import PostType, PostImage
from posts.models import Post
from django.core.cache import cache
from globals.middlewares import JWTAuthenticaton_GraphQL

class Query(graphene.ObjectType):
    user_timeline = graphene.List(PostType)
    get_post_by_id = graphene.Field(PostType, post_id=graphene.Int(required=True))
    get_post_by_owner_username = graphene.List(PostType, post_owner_username=graphene.String(required=True))

    @JWTAuthenticaton_GraphQL
    def resolve_user_timeline(self, user, info, **kwargs):
        if not user.is_authenticated:
            raise Exception("Authentication required")

        posts = cache.get("posts",None)

        if not posts:
            posts = Post.objects.all()
            cache.set('posts', posts)

        return posts.filter(owner__in=user.followings.all()).order_by('-created_at').order_by('likes_by_counter')


    def resolve_get_post_by_id(self, info, post_id, **kwargs):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise Exception("Post not found")

        return post
    
    def resolve_get_post_by_owner_username(self, info, post_owner_username, **kwargs) : 
        return Post.objects.filter(owner__username=post_owner_username)
            

posts_schema = graphene.Schema(query=Query)
