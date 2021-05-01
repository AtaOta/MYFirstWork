import random
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from Account.models import User
from Account.models import NormalProfile, SellerProfile, ServiceProviderProfile


Profile_Background_Images = {
    1: '/Default/BackgroundImg/BackgroundPic1.png',
    2: '/Default/BackgroundImg/BackgroundPic2.png',
    3: '/Default/BackgroundImg/BackgroundPic3.png',
    4: '/Default/BackgroundImg/BackgroundPic4.png',
    5: '/Default/BackgroundImg/BackgroundPic5.png',
    6: '/Default/BackgroundImg/BackgroundPic6.png'
}


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        NormalProfile.objects.create(
            user=instance,
            name=instance.full_name,
            profile_pick="/Default/NormalProfile_Img.png",
            profile_Background_pic=Profile_Background_Images[random.randint(1, 6)]
        )

        SellerProfile.objects.create(user=instance,
                                     Seller_name=instance.full_name,
                                     Seller_Profile_pick="/Default/SellerProfile.png")

        ServiceProviderProfile.objects.create(user=instance,
                                              SerV_name=instance.full_name,
                                              SerV_Profile_pick="/Default/SeviceProfile.png")


