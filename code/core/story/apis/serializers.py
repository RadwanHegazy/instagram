from ..models import Story
from ..tasks import story_builder
from rest_framework import serializers
from users.apis.serializres import UserSerializer
import json
from uuid import uuid4
from django.core.files.storage import FileSystemStorage

class GetStorySerializer (serializers.ModelSerializer) :
    owner = UserSerializer()
    
    class Meta:
        model = Story
        fields = '__all__'

class CreateStorySerializer (serializers.Serializer) : 
    text_list = serializers.CharField()
    image = serializers.ImageField()
    
    class Meta:
        fields = [
            'text_list',
            'image',
        ]
    
    def validate(self, attrs):
        attrs['user_id'] = self.context.get('user').id
        attrs['text_list'] = json.loads(attrs['text_list'])
        return attrs

    def save(self, **kwargs):
        text_list = self.validated_data['text_list']
        text_list = [dict(i) for i in text_list]

        image_obj = self.validated_data['image']
        user_id = self.validated_data['user_id']

        saved_image = FileSystemStorage(
            location="media/story-imgs/"
        )
        
        saved_image = saved_image.save(
            image_obj.name,
            image_obj
        )

        img_path = f"/media/story-imgs/{saved_image}"
        
        story_builder.delay(
            user_id=user_id,
            text_list=text_list,
            image=img_path
        )

    def to_representation(self, instance):
        return {}