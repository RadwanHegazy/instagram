
def custom_save_data(*args, **kwargs) : 
    from users.models import User
    user = kwargs['user'] # the incomming user from the social platfrom
    u, _ = User.objects.get_or_create(
        username=user['email'].split('@')[0],
        email=user['email'],
        extra_fields = kwargs
    )
    u.save()
    return u