from django.shortcuts import render
from SellerPro.models import Product, Order


def ataota_home(request):
    if request.user.is_authenticated:
        customer = request.user.normalprofile
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']
    all_products = Product.objects.all()
    return render(request, 'ataota/Home.html',
                  {"products": all_products,
                   "cartItems": cartItems
                   })


