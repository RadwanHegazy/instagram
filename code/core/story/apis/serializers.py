from ..models import Story
from ..tasks import story_builder
from rest_framework import serializers
from users.apis.serializres import UserSerializer


class GetStorySerializer (serializers.ModelSerializer) :
    owner = UserSerializer()
    
    class Meta:
        model = Story
        fields = '__all__'

class CreateStorySerializer (serializers.Serializer) : 
    controls = serializers.JSONField()
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    
    class Meta:
        fields = [
            'controls',
            'image',
            'video'
        ]
    
    def validate(self, attrs):
        attrs['user'] = self.context.get('user')
        return attrs

    def save(self, **kwargs):
        story_builder.delay(**self.validated_data)


    def to_representation(self, instance):
        return {
            'message' : "story created"
        }