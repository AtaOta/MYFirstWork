from django.contrib.auth import get_user_model
from django.contrib import admin
User = get_user_model()

from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from Account.models import User, NormalProfile, FollowersFollowing, SellerProfile, ServiceProviderProfile, UserOTP


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    model = User
    list_display = ('username', 'full_name', 'email', 'phone', 'is_staff', 'is_active')
    list_filter = ('username', 'full_name', 'email', 'phone', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'email', 'phone', 'password1',  'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('username', 'full_name', 'email', 'phone',)
    ordering = ('email',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)
admin.site.register(NormalProfile)
admin.site.register(SellerProfile)
admin.site.register(ServiceProviderProfile)
admin.site.register(FollowersFollowing)
admin.site.register(UserOTP)
