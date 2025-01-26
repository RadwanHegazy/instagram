from django.urls import path
from .views import get, delete, create

urlpatterns = [
    path('get/', get.PostListsView.as_view(),name='all_posts'),
    path('get/<int:id>/', get.RetrivePostView.as_view(),name='get_post_by_id'),
    path('delete/<int:id>/', delete.DeletePostView.as_view(),name='delete_post_by_id'),
    path('create/', create.CreatePostView.as_view(),name='create_post'),
]