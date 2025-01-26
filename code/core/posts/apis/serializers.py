from rest_framework import serializers
from ..models import Post, User, PostImage

class PostUserSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = User
        fields = [
            'id'
            'username',
            'full_name',
            'picture',
        ]

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
            'created_at'
        ]

class CreatePostSerializer (serializers.ModelSerializer) : 
    
    class Meta:
        model = Post
        fields = ['body']

    def validate(self, attrs):
        attrs['owner'] = self.context.get('owner')
        return attrs
    
    def save(self, **kwargs):
        post_model = Post.objects.create(**self.validated_data)
        images = self.context.get('images', [])
        for img in images:
            img_model = PostImage.objects.create(
                image=img
            )
            img_model.save()
            post_model.images.add(img_model)
        post_model.save()
        return post_model
        