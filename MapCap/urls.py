from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_map, name="Map_Page"),
    path('NormalProfile_Map', views.normal_profile_map, name="NormalProfile_Map"),
]
