"""ataota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ataota_home, name="HomePage"),

    path('Account/', include('Account.urls')),
    path('profile/', include('NormPro.urls')),
    path('chatting/', include('ChatSon.urls')),
    path('serviceProvider/', include('ServPro.urls')),
    path('seller/', include('SellerPro.urls')),
    path('MapPage/', include('MapCap.urls')),
    path('AboutAtaOta/', include('AboutUs.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

