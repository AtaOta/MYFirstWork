from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Normal In-build Import
from django.contrib import messages
import json

# Spacial In-build Import
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from Account.models import User

# Created Import
from Account.models import SellerProfile
from .models import Product, Order, OrderedItem

# =================[ This is for decorators ]==================
from Account.Acc_MethodDecorator import login_user_only, seller_only
decorators = [login_user_only]
serv_decorators = [login_user_only, seller_only]


@login_user_only
@seller_only
def seller_pfofile_view(request, pk):
    products = Product.objects.filter(prod_uploded_by=request.user.sellerprofile)
    print(products)
    return render(request, 'SellerPro/Service_Provider_Profile_Related/Seller_Profile.html',
                  {
                      'products': products
                  })


# User Profile Update Section
@method_decorator(decorators, name='dispatch')
class SellerProfileUpdateView(UpdateView):
    """
    ~~~~~~~~~: This Section is Help Us to Update An User Normal Profile :~~~~~~~~~
    """
    model = SellerProfile
    template_name = 'SellerPro/Service_Provider_Profile_Related/Seller_Profile_Update.html'
    # ServPro/Service_Provider_Profile_Related/NewTest.html
    # ServPro/Service_Provider_Profile_Related/Seller_Profile_Update.html
    fields = ["Seller_name",
              "Seller_Store_name",
              "Seller_Store_type",
              "Seller_particular_profession",
              "Seller_birth_date",
              "Seller_age",
              "Seller_address",
              "Seller_phone_no",
              "Seller_gender",
              "Seller_Profile_pick"]

    def form_valid(self, form):
        self.object = form.save()
        self.object = self.request.user.serviceproviderprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, f"Dear {self.request.user.serviceproviderprofile.SerV_name}" 
                                       f" Your Seller Account Created Successfully")
        return f"/profile/NormalProfile/{self.request.user.id}/"


@login_user_only
@seller_only
def upload_products(request):
    serv_details = SellerProfile.objects.filter(user=request.user)
    return HttpResponse('This is product upload page')


@method_decorator(serv_decorators, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    template_name = 'SellerPro/Product_Related/Product_Upload.html'
    fields = ["prod_name",
              "prod_picture",
              "prod_price",
              "quantity",
              "in_terms_of",
              "country_Of_Origin",
              "prod_description",
              "prod_offer"]

    def form_valid(self, form):
        self.object = form.save()
        self.object.prod_uploded_by = self.request.user.sellerprofile
        # print(self.object.prod_uploded_by)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, f"{self.request.user.sellerprofile.Seller_name},"
                                       f" You Successfully Upload Your Product")
        return f"/"


def cart_page(requests):
    if requests.user.is_authenticated:
        customer = requests.user.normalprofile
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.ordereditem_set.all().order_by('-id')
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']
    context = {'items': items, 'order': order, "cartItems": cartItems}
    return render(requests, "SellerPro/Product_Cart/Shopin_Cart.html", context)


# ==================================
# This request for update cart page
# ==================================
def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('productId:', productId)
    print('action:', action)
    customer = request.user.normalprofile
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderedItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    cartItems = order.get_cart_item
    ItemData = [{'ItemQuantity': cartItems}]
    return JsonResponse(json.dumps(ItemData), safe=False)


def remove_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.normalprofile
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    cart_product, created = OrderedItem.objects.get_or_create(id=productId, order=order)

    if action == 'remove':
        cart_product.quantity = (cart_product.quantity - 1)
        cart_product.save()

        if cart_product.quantity <= 0:
            cart_product.delete()
            cartItems = order.get_cart_item
            ItemData = [{'SetItem': 'Removed', 'ItemQuantity': cartItems}]
            return JsonResponse(json.dumps(ItemData), safe=False)

        cartItems = order.get_cart_item
        ItemData = [{'SetItem': cart_product.quantity, 'ItemQuantity': cartItems}]
        return JsonResponse(json.dumps(ItemData), safe=False)



