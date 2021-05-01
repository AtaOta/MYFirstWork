from django.urls import path
from . import views
from NormPro.views import NormalProfileView, UserNormalPostList, NormalProfileUpdateView, \
    NormalPostCreateView

urlpatterns = [
    # =========================[ Normal Profile Objects Section ]=======================
    path('NormalProfile/<int:pk>/', NormalProfileView.as_view(), name='Normal_User_Profile'),
    path('Normal_Profile_Update/<int:pk>/', NormalProfileUpdateView.as_view(), name="Normal_Profile_Update"),

    # =========================[ Change Profile Picture By Capturing ]=======================
    path('CaptureYourImage', views.change_picture_by_capturing, name='Capture_Your_Image'),
    path('CaptureNormalPost', views.create_post_by_capturing, name='Capture_Create_Normal_Post'),

    # =========================[ User Posts Section ]=======================
    path('MyPost/', UserNormalPostList.as_view(), name="MY_Post"),
    path('Normal_Post_create/<int:pk>/', NormalPostCreateView.as_view(), name='Normal_Post_create'),
    path('DeleteNormalPost/<int:pk>/', views.normal_post_delete, name='Delete_Normal_Post'),
    path('Create_comment', views.create_normalPost_comment, name='Creating_NormalPost_Comment'),
    path('List_comment/<int:pk>', views.normal_post_comment_list, name='NormalPost_Comment_List'),
    path('Normal_Post_Like_Dislike/<int:pk>/', views.normalpost_like_dislike, name='Normal_Post_Like_Dislike'),

]

