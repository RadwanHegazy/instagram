from posts.models import User, Post

def get_user_timline(
    user : User,
    posts : list[Post]
) : 
    timeline = []
    for post in posts:
        if post.owner in user.followings.all() : 
            timeline.append(post)
            