from django.urls import path
from . import views


urlpatterns = [
    path('About_Us/', views.about_us, name="aboutUs"),
]
