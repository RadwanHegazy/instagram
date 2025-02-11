from rest_framework_simplejwt.tokens import AccessToken
from posts.models import Post
from story.models import Story, User
from chat.models import Chat, Message
from notifications.models import Notification

def create_user (
        username = 'test',
        password='test',
        email='test@gmail.com'
):
    user = User.objects.create(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def create_notification(sender, reciver, content='test') : 
    return Notification.objects.create(sender=sender, reciver=reciver, content=content)

def create_chat(u1 : User,  u2 : User) -> Chat:
    c = Chat.objects.create()
    c.users.add(u1)
    c.users.add(u2)
    c.save()
    return c

def create_message (sender : User, content : str, chat : Chat) -> Message : 
    return Message.objects.create(sender=sender, content=content, chat=chat)

def create_story(user) -> Story:
    return Story.objects.create(
        owner=user,
    ) 

def create_access_token(user=None) : 
    if not user :
        user = create_user()

    return str(AccessToken.for_user(user))


def create_token_headers(user=None) : 
    if not user:
        user = create_user()
    
    tokens = create_access_token(user)

    return {
        'Authorization' : f"Bearer {tokens}"
    }


def create_post(user=None) : 
    if not user:
        user = create_user()

    p = Post.objects.create(
        body='test',
        owner=user
    )
    p.save()
    return p