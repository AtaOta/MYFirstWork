from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import SignUp


urlpatterns = [
    # path('', SignUp.as_view(), name="SignUp"),
    path('SignUp/', views.sign_up, name="SignUp"),
    path('Login/', views.log_in, name="Login"),
    path('Logout/', views.handleLogout, name="LogOut"),

    # This Section is for Password Change:
    path(
            'password_change/', views.password_change,
            name='password_change'
        ),

    path(
            'password_change/done/', 
            auth_views.PasswordChangeDoneView.as_view(template_name='ataota/Home.html'),
            name='password_change_done'
        ),

    # This Section is for Password Reset Purpose:
    path(
            'reset_password/', 
            auth_views.PasswordResetView.as_view(template_name='Account/password-reset.html'),
            name="reset_password"
        ),
    
    path(
            'reset_password_sent/', 
            auth_views.PasswordResetDoneView.as_view(template_name='Account/email_send_password_reset.html'),
            name="password_reset_done"
        ),

    path(
            'reset/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(template_name='Account/password_reset_form.html'),
            name="password_reset_confirm"
        ),

    path(
            'reset_password_complete/', 
            auth_views.PasswordResetCompleteView.as_view(template_name ='Account/Login.html'), 
            name="password_reset_complete"
        ),

    # =========================[ All Users List ]=======================
    path('Users_lists/', views.user_list, name='All_Users_List'),
    path('user_follow_un_follow/<int:pk>', views.user_follow_un_follow, name='Follow_UnFollow'),
]

