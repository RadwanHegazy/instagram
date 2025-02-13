from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from globals.validators import check_email_or_phonenumber
from rest_framework.validators import ValidationError

class TokenSerializer:

    def to_representation(self, instance=None):
        tokens = RefreshToken.for_user(self.user)
        return {
            'refresh_token' : str(tokens),
            'access_token' : str(tokens.access_token),
        }


class RegisterSerializer (TokenSerializer, serializers.ModelSerializer) : 
    
    class Meta:
        model = User
        fields = ['username','phonenumber','full_name','email','picture','password']


    def save(self, **kwargs):
        password = self.validated_data.pop('password')
        user = User.objects.create(
            **self.validated_data
        )
        user.set_password(password)
        user.save()
        self.user = user
        return user
    

class LoginSerializer (TokenSerializer, serializers.Serializer) : 
    email_or_phonenumber = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email_or_phonenumber = attrs['email_or_phonenumber']
        password = attrs['password']
        
        user_key = check_email_or_phonenumber(email_or_phonenumber)

        try : 
            self.user = User.objects.get(**user_key)
        except User.DoesNotExist:
            raise ValidationError({
                'message' : "invalid authentication"
            })

        if not self.user.check_password(password) : 
            raise ValidationError({
                'message' : "invalid authentication"
            })

        return self.user
    
    def save(self, **kwargs): ...
    

class ProfileSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = User
        exclude = ['password']
    
class UserSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name',
            'picture',
        ]


class BaseFollowUserSerializer (serializers.Serializer) : 
    follow_user_id = serializers.IntegerField()

    def validate(self, attrs):
        follow_user_id = attrs.get('follow_user_id')
        user = self.context.get('user')

        follow_user = User.objects.filter(id=follow_user_id)

        if not follow_user.exists() or follow_user_id == user.id:
            raise ValidationError({
                'message' : 'invalid user id'
            })
        
        attrs['follow_user'] = follow_user.first()
        attrs['user'] = user
        return attrs
    
    def to_representation(self, instance):
        return {}

class FollowUserSerializer (BaseFollowUserSerializer) : 

    def save(self, **kwargs):
        follow_user:User = self.validated_data.get('follow_user')
        user:User = self.validated_data.get('user')

        if user not in follow_user.followers.all() : 
            follow_user.followers.add(user)
            follow_user.followers_count += 1

            user.followings.add(follow_user)
            user.following_count += 1

            user.save()
            follow_user.save()
            
            from globals.notifications import FollowNotification

            notificaion = FollowNotification(
                sender=user,
                reciver=follow_user
            )
            
            notificaion.send()

class UnFollowUserSerializer (BaseFollowUserSerializer) : 

    def save(self, **kwargs):
        follow_user:User = self.validated_data.get('follow_user')
        user:User = self.validated_data.get('user')

        if user in follow_user.followers.all() : 
            follow_user.followers.remove(user)
            follow_user.followers_count -= 1

            user.followings.remove(follow_user)
            user.following_count -= 1

            user.save()
            follow_user.save()
