from rest_framework import serializers
from ..models import Post, User, PostImage
from rest_framework.validators import ValidationError
from users.apis.serializres import UserSerializer as PostUserSerializer
from globals.notifications import LikePostNotification

class PostImagesSerializer (serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'

class PostsSerializer (serializers.ModelSerializer) : 
    owner = PostUserSerializer()
    created_at = serializers.DateTimeField()
    images = PostImagesSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'owner',
            'body',
            'likes_by_counter',
            'created_at',
            'images'
        ]

class CreatePostSerializer (serializers.ModelSerializer) : 
    
    class Meta:
        model = Post
        fields = ['id','body']

    def validate(self, attrs):
        attrs['owner'] = self.context.get('owner')
        images = self.context.get('images', [])
        
        if not any(images) :
            raise ValidationError({
                'message' : "no images found"
            })
        
        attrs['images'] = images
        return attrs
    
    def save(self, **kwargs):
        images = self.validated_data.pop('images')
        post_model = Post.objects.create(**self.validated_data)

        for img in images:
            img_model = PostImage.objects.create(
                image=img
            )
            img_model.save()
            post_model.images.add(img_model)

        post_model.save()
        return post_model
        

class UpdatePostSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Post
        fields = ['body']


class BaseLikePostSerializer (serializers.Serializer) : 
    post_id = serializers.IntegerField()

    def validate(self, attrs):
        post_id = attrs.get('post_id')
        
        try : 
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise ValidationError({
                'message' : "post not found for this id"
            }, code=404)
        
        attrs['post'] = post
        attrs['liked_by'] = self.context.get('user')

        return attrs

    def to_representation(self, instance):
        return {}

class LikePostSerializer (BaseLikePostSerializer) : 
    
    def save(self, **kwargs):
        post:Post = self.validated_data.get('post')
        liked_by:User = self.validated_data.get('liked_by')

        if liked_by not in post.likes_by.all() : 
            post.likes_by_counter += 1
            post.likes_by.add(liked_by)
            post.save()

            notification = LikePostNotification(
                sender=liked_by,
                reciver=post.owner
            )
            notification.send()

        return post
    
 

class RemoveLikePostSerializer (BaseLikePostSerializer) : 

    def save(self, **kwargs):
        post:Post = self.validated_data.get('post')
        liked_by:User = self.validated_data.get('liked_by')

        if liked_by in post.likes_by.all() : 
            post.likes_by_counter -= 1
            post.likes_by.remove(liked_by)
            post.save()

        return post
    