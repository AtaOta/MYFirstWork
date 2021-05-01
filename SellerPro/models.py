from django.db import models
from Account.models import NormalProfile, SellerProfile
from django.core.validators import MinValueValidator, MaxValueValidator


Quantity_In_Terms_Of = (
    ('Kg', 'Kg'),
    ('L', 'L'),
    ('Pack', 'Pack'),
    ('Piece', 'Piece'),
    ('Quarter', 'Quarter'),
    ('Square cm', 'Square cm'),
    ('Square m', 'Square m'),
    ('Unit', 'Unit'),
    ('cm', 'cm'),
    ('db', 'db'),
    ('dozen', 'dozen'),
    ('ft', 'ft'),
    ('gallon', 'gallon'),
    ('gm', 'gm'),
    ('inch', 'inch'),
    ('m', 'm'),
    ('mg', 'mg'),
    ('ml', 'ml'),
    ('mm', 'mm'),
    ('pound', 'pound'),
    ('square ft', 'square ft'),
    ('tone', 'tone'),
    ('watt', 'watt'),
)
Product_Country_Of_Origin = (
    ('Australia', 'Australia'),
    ('Bangladesh', 'Bangladesh'),
    ('Belgium', 'Belgium'),
    ('Germany', 'Germany'),
    ('Hong Kong', 'Hong Kong'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Iran', 'Iran'),
    ('Iraq', 'Iraq'),
    ('Israel', 'Israel'),
    ('Japan', 'Japan'),
    ('Kuwait', 'Kuwait'),
    ('Malaysia', 'Malaysia'),
    ('Nepal', 'Nepal'),
    ('Netherlands', 'Netherlands'),
    ('Nigeria', 'Nigeria'),
    ('Qatar', 'Qatar'),
    ('Russia', 'Russia'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Singapore', 'Singapore'),
    ('Singapore', 'Singapore'),
    ('South Africa', 'South Africa'),
    ('South Korea', 'South Korea'),
    ('Switzerland', 'Switzerland'),
    ('UAE', 'UAE'),
    ('UK', 'UK'),
    ('US', 'US'),
    ('Venezuela', 'Venezuela')
)


# ______________________________________________________________________
#               That Is Product section [product create]
# ______________________________________________________________________
class Product(models.Model):
    prod_name = models.CharField(max_length=255)
    prod_picture = models.ImageField(upload_to='products/images')
    prod_price = models.FloatField(default=0, validators=[MinValueValidator(0)], max_length=20)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    in_terms_of = models.CharField(max_length=10, default="Kg", choices=Quantity_In_Terms_Of)
    country_Of_Origin = models.CharField(max_length=25, default="India", choices=Product_Country_Of_Origin)
    prod_description = models.TextField()
    prod_offer = models.IntegerField(default=0,
                                     validators=[MinValueValidator(0), MaxValueValidator(100)],
                                     null=True, blank=True
                                     )
    creat_date = models.DateTimeField(auto_now_add=True)
    prod_uploded_by = models.ForeignKey(to=SellerProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s' % self.prod_name + " | upload by: " + str(self.prod_uploded_by) + \
               " | Quantity: " + str(self.quantity) + "-" + str(self.in_terms_of)

    def save(self, *args, **kwargs):
        """
        This part is very important for uploading a file because
        It will replace the previous file and insert the new file.
        :return: delete old file when replacing by updating the file
        """
        try:
            this = Product.objects.get(id=self.id)
            if this.profile_pick != self.prod_picture:
                this.profile_pick.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Product, self).save(*args, **kwargs)


# ______________________________________________________________________
#                 That Is Product Order Section
# ______________________________________________________________________
class Order(models.Model):
    customer = models.ForeignKey(to=NormalProfile, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_item = self.ordereditem_set.all()
        total = sum([item.get_total for item in order_item])
        return total

    @property
    def get_cart_item(self):
        order_item = self.ordereditem_set.all()
        total = sum([item.quantity for item in order_item])
        return total


# ______________________________________________________________________
#                That Is Product Order List Items
# ______________________________________________________________________
class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    in_terms_of = models.CharField(max_length=10, default="Kg", choices=Quantity_In_Terms_Of)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.product

    @property
    def get_total(self):
        total = self.product.prod_price * self.quantity
        return total

    def save(self, *args, **kwargs):
        """
        This part is very important for uploading a file because
        It will replace the previous file and insert the new file.
        :return: delete old file when replacing by updating the file
        """
        try:
            this = OrderedItem.objects.get(id=self.id)
            this.in_terms_of = str(self.product.in_terms_of)
        except:
            pass
        super(OrderedItem, self).save(*args, **kwargs)



