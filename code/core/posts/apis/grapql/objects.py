from graphene_django.types import DjangoObjectType
from posts.models import Post, PostImage
from users.models import User


class PostOwnerType(DjangoObjectType) : 
    class Meta:
        model = User
        fields = ['id','username','picture']

class PostImageType(DjangoObjectType):
    class Meta:
        model = PostImage
        fields = ("id", "image")

class PostType(DjangoObjectType):
    images = PostImageType()
    owner = PostOwnerType()
    class Meta:
        model = Post
        fields = ("id", "owner", "created_at", "updated_at", "body", "likes_by_counter", "images")

