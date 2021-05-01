from django.db import models

#  Crate Custom User Model
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a Superuser with the given email and Password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number format '+919999999999' ")
    phone = models.CharField('Phone', validators=[phone_regex], max_length=10, unique=True, null=True, blank=True)
    full_name = models.CharField(default="", max_length=255, blank=True)
    REQUIRED_FIELD = ['username', 'full_name']

    object = UserManager()


class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now=True)
    otp = models.SmallIntegerField()


class NormalProfile(models.Model):
    """
    This is "ALL USERS PROFILE" Model
    """
    name = models.CharField(max_length=50)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    age = models.IntegerField(default=12, validators=[MinValueValidator(12)])
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default="I use this app to help others...", null=True, blank=True)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],
                                max_length=15,
                                null=True,
                                blank=True
                                )
    description = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10,
                              default="Male",
                              choices=(("Male", "Male"),
                                       ("Female", "Female"),
                                       ("TransGen", "TransGen")
                                       )
                              )
    profile_pick = models.ImageField(upload_to='Profile/images',
                                     null=True, blank=True
                                     )
    profile_Background_pic = models.ImageField(upload_to='Profile/background_Image',
                                               null=True, blank=True
                                               )

    def __str__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        """
        This part is very important for uploading a file because
        It will replace the previous file and insert the new file.
        :return: delete old file when replacing by updating the file
        """
        try:
            this = NormalProfile.objects.get(id=self.id)
            if this.profile_pick != self.profile_pick:
                this.profile_pick.delete(save=False)
            if this.profile_Background_pic != self.profile_Background_pic:
                this.profile_Background_pic.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(NormalProfile, self).save(*args, **kwargs)


# =========================[ User Follow-UnFollow Section ]=======================
class FollowersFollowing(models.Model):
    """
    Followers, Following By, Un Follow etc. Of an User.
    """
    followed_by = models.ManyToManyField(to=User, related_name='following', symmetrical=False)
    following_user = models.OneToOneField(to=User, unique=True, on_delete=models.CASCADE)

    # This is for Follow purpose
    @classmethod
    def follow(cls, following_user, followed_by_user):
        obj, create = cls.objects.get_or_create(following_user=following_user)
        obj.followed_by.add(followed_by_user)

    # This is for Un-Follow purpose
    @classmethod
    def un_follow(cls, following_user, followed_by_user):
        obj, create = cls.objects.get_or_create(following_user=following_user)
        obj.followed_by.remove(followed_by_user)

    @property
    def get_total_following(self):
        all_follower_users = FollowersFollowing.objects.filter(followed_by=self.following_user)
        total_following_number = all_follower_users.count()
        return total_following_number

    @property
    def get_total_followers(self):
        total_followers_number = self.followed_by.count()
        return total_followers_number

    @property
    def get_user(self):
        new_user = self
        return self

    def __str__(self):
        return "Followers Of: " + str(self.following_user)


# ______________________________________________________________________
#                 That Is Seller Profile Section
# ______________________________________________________________________
class SellerProfile(models.Model):
    """
    This is "SERVICE PROVIDER PROFILE" MODEL
    Here (SerV) => (service provider)
    """
    Seller_name = models.CharField(max_length=50)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    Seller_Store_name = models.CharField(max_length=100)
    Seller_Store_type = models.CharField(max_length=100,
                                              default="Grocery",
                                              choices=(
                                                  ("Grocery", "Grocery"),
                                                  ("Farm", "Farm"),
                                                  ("Medical", "Medical"),
                                                  ("Educational Product", "Educational Product"),
                                                  ("Electronics", "Electronics"),
                                                  ("", "Tech"),
                                              ))
    Seller_particular_profession = models.CharField(max_length=255)
    Seller_birth_date = models.DateField(null=True)
    Seller_age = models.IntegerField(default=12, validators=[MinValueValidator(12), MaxValueValidator(80)])
    Seller_address = models.CharField(max_length=255, default='')
    # SerV_location_lat = models.DecimalField(max_length=12)
    # SerV_location_lng = models.DecimalField(max_length=12)
    Seller_phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15)
    Seller_gender = models.CharField(max_length=10,
                              default="Male",
                              choices=(("Male", "Male"),
                                       ("Female", "Female"),
                                       ("TransGen", "TransGen")
                                       )
                              )
    Seller_Profile_pick = models.ImageField(upload_to='SellerProfile/ProfileImages')

    def __str__(self):
        return '%s' % self.Seller_name

    def save(self, *args, **kwargs):
        """
        This part is very important for uploading a file because
        It will replace the previous file and insert the new file.
        :return: delete old file when replacing by updating the file
        """
        try:
            this = SellerProfile.objects.get(id=self.id)
            if this.SerV_Profile_pick != self.Seller_Profile_pick:
                this.SerV_Profile_pick.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(SellerProfile, self).save(*args, **kwargs)


# ______________________________________________________________________
#                 That Is Service Provider Profile Section
# ______________________________________________________________________
class ServiceProviderProfile(models.Model):
    """
    This is "SERVICE PROVIDER PROFILE" MODEL
    Here (SerV) => (service provider)
    """
    SerV_name = models.CharField(max_length=50)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    SerV_institutions_name = models.CharField(max_length=100)
    SerV_service_type = models.CharField(max_length=100,
                                              default="Grocery",
                                              choices=(
                                                  ("Grocery", "Grocery"),
                                                  ("Farm", "Farm"),
                                                  ("Medical", "Medical"),
                                                  ("Teaching", "Teaching"),
                                                  ("Transportation", "Transportation"),
                                                  ("Tech", "Tech"),
                                              ))
    SerV_particular_profession = models.CharField(max_length=255)
    SerV_birth_date = models.DateField(null=True)
    SerV_age = models.IntegerField(default=12, validators=[MinValueValidator(12), MaxValueValidator(80)])
    SerV_address = models.CharField(max_length=255, default='')
    # SerV_location_lat = models.DecimalField(max_length=12)
    # SerV_location_lng = models.DecimalField(max_length=12)
    SerV_phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15)
    SerV_gender = models.CharField(max_length=10,
                              default="Male",
                              choices=(("Male", "Male"),
                                       ("Female", "Female"),
                                       ("TransGen", "TransGen")
                                       )
                              )
    SerV_Profile_pick = models.ImageField(upload_to='ServProfile/ProfileImages')

    def __str__(self):
        return '%s' % self.SerV_name

    def save(self, *args, **kwargs):
        """
        This part is very important for uploading a file because
        It will replace the previous file and insert the new file.
        :return: delete old file when replacing by updating the file
        """
        try:
            this = ServiceProviderProfile.objects.get(id=self.id)
            if this.SerV_Profile_pick != self.SerV_Profile_pick:
                this.SerV_Profile_pick.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(ServiceProviderProfile, self).save(*args, **kwargs)

