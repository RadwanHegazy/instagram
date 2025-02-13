from django.urls import path
from .views import delete, create, update
from .grapql.schema import posts_schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path('get/', GraphQLView.as_view(graphiql=True, schema=posts_schema),name='all_posts'),
    path('delete/<int:id>/', delete.DeletePostView.as_view(),name='delete_post_by_id'),
    path('update/<int:id>/', update.UpdatePostView.as_view(),name='update_post_by_id'),
    path('create/', create.CreatePostView.as_view(),name='create_post'),
    path('love/add/', create.LovePostView.as_view(), name='add_love'),
    path('love/remove/', create.RemoveLovePostView.as_view(), name='remove_love'),

]