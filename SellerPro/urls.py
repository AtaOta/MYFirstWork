from django.urls import path
from . import views
from .views import SellerProfileUpdateView, ProductCreateView

urlpatterns = [
    path("Seller_Profile/<int:pk>/",
         views.seller_pfofile_view,
         name='Seller_Profile'),

    path('Seller_Profile_Update/<int:pk>/',
         SellerProfileUpdateView.as_view(), name="Seller_Profile_Update"),

    # Test Case
    path("Product_Upload", views.upload_products, name="Product_Uploading"),

    path("Product_Upload/<int:pk>/", ProductCreateView.as_view(), name="Product_Create"),

    # =========================[ Shoping Cart Page ]=======================
    path('Shoping_Cart/', views.cart_page, name='Shoping_Cart'),
    path('update_cart_item/', views.update_item, name='Update_Cart_Item'),
    path('remove_cart_item/', views.remove_item, name='remove_Cart_Item'),
]