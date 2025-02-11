from django.urls import path
from .views import get, delete

urlpatterns = [
    path('get/', get.ListNotificationsAPI.as_view(), name='get_notifications'),
    path('delete/<int:id>/', delete.DeleteNotificationsAPI.as_view(), name='delete_notification'),
]