from django.urls import path
from . import views

urlpatterns = [
    path('followingList', views.following_list, name='Following_User_List'),
    path('followersList', views.followers_list, name='Followers_User_List'),

    # =========================[ Chat List ]=======================
    path('Chatting_userList', views.chat_list, name='ChatList'),
    path('create_chat/<int:pk>', views.chat_son_chat, name="Create_Chat"),
    path('chat_message_list/<int:pk>', views.chat_msg_list, name="Chat_Message_List"),
]
