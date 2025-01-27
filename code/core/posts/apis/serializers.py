from rest_framework import serializers
from ..models import Post, User, PostImage
from rest_framework.validators import ValidationError

class PostUserSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = User
        fields = [
            'id',
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
