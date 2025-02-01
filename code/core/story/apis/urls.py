from django.urls import path
from .views import create, get, delete

urlpatterns = [
    path('get/', get.ListStoriesView.as_view(), name='get_stories'),
    path('get/<int:id>/', get.RetriveStoryById.as_view(), name='get_story'),
    path('create/', create.CreateStoryView.as_view(),name='create_story'),
    path('delete/<int:id>/', delete.DeleteStoryView.as_view(), name='delete_story'),
]