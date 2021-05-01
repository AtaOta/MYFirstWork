from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Normal In-build Import
from django.contrib import messages
import json

# Spacial In-build Import
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User

# Created Import
from Account.models import ServiceProviderProfile

# =================[ This is for decorators ]==================
from Account.Acc_MethodDecorator import login_user_only
decorators = [login_user_only]
serv_decorators = [login_user_only]


# def service_provider_profile(request, pk):
#     return render(request, 'ServPro/Service_Provider_Profile_Related/Seller_Profile_Update.html')


# def service_prvider_pfofile_view(request, pk):
#     products = Product.objects.filter(prod_uploded_by=request.user.serviceproviderprofile)
#     print(products)
#     return render(request, 'ServPro/Service_Provider_Profile_Related/Seller_Profile.html',
#                   {
#                       'products': products
#                   })


# User Profile Update Section
@method_decorator(decorators, name='dispatch')
class ServiceProviderProfileUpdateView(UpdateView):
    """
    ~~~~~~~~~: This Section is Help Us to Update An User Normal Profile :~~~~~~~~~
    """
    model = ServiceProviderProfile
    template_name = 'ServPro/Service_Provider_Profile_Related/Service_Provider_Profile_Update.html'
    # ServPro/Service_Provider_Profile_Related/NewTest.html
    # ServPro/Service_Provider_Profile_Related/Seller_Profile_Update.html
    fields = ["SerV_name",
              "SerV_institutions_name",
              "SerV_service_type",
              "SerV_particular_profession",
              "SerV_birth_date",
              "SerV_age",
              "SerV_address",
              "SerV_phone_no",
              "SerV_gender",
              "SerV_Profile_pick"]

    def form_valid(self, form):
        self.object = form.save()
        self.object = self.request.user.serviceproviderprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, f"Dear {self.request.user.serviceproviderprofile.SerV_name}" 
                                       f" Your Service Account Created Successfully")
        return f"/profile/NormalProfile/{self.request.user.id}/"


# @login_user_only
# @service_provider_only
# def upload_products(request):
#     serv_details = ServiceProviderProfile.objects.filter(user=request.user)
#     return HttpResponse('This is product upload page')


# @method_decorator(serv_decorators, name='dispatch')

