from django.urls import path
from . import views
from .views import ServiceProviderProfileUpdateView

urlpatterns = [
    # path("Service_Provider_Profile/<int:pk>/",
    #      views.service_prvider_pfofile_view,
    #      name='Service_Provider_Profile'),

    path('ServiceProvider_Profile_Update/<int:pk>/',
         ServiceProviderProfileUpdateView.as_view(), name="ServiceProvider_Profile_Update"),

    # Test Case

]

