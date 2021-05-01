from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import SellerProfile


def login_user_only(view_func):
    """:~~~:[ This function is checking is user login (authenticated) or not ]:~~~: """
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('Login'))
    return wrap


def seller_only(view_func):
    """ :~~~:[ This function is checking is user has an service provider profile or not ]:~~~: """
    def wrap(request, *args, **kwargs):
        seller_details = SellerProfile.objects.filter(user=request.user)
        for seller_detail in seller_details:
            if (seller_detail.Seller_Store_name != '') & (seller_detail.Seller_Store_type != '') \
                    & (seller_detail.Seller_particular_profession != '') & (seller_detail.Seller_birth_date != '')\
                    & (seller_detail.Seller_address != '') & (seller_detail.Seller_phone_no != ''):
                return view_func(request, *args, **kwargs)
            else:
                messages.info(request, "Please Create Your 'Seller Profile' First.")
                return HttpResponseRedirect(f'/seller/Seller_Profile_Update/{request.user.id}/')
    return wrap




