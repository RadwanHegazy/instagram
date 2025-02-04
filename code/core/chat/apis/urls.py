from .views.chat import get as get_chat

from .views.message import get as get_msg, delete as del_msg

from django.urls import path

urlpatterns = [
    path('get/', get_chat.ChatListView.as_view(), name='user_chats'),
    path('get/<int:chat_id>/', get_msg.RetriveChatMessageAPI.as_view(), name='get_chat_msgs'),
    path('delete/message/<int:id>/', del_msg.DeleteMessageAPI.as_view(), name='delete_msg'),

]