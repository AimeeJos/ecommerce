from djongo import models
from django.contrib.auth.models import User


# user types
user_types=(
    ('S','shop'),
    ('C','customer'),
)

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField()
    usertype=models.CharField(max_length=1,choices=user_types)


    def __str__(self):
        return self.name



class AboutShop(models.Model):
    shop_id = models.AutoField(primary_key=True,unique=True)
    userid = models.ForeignKey(Customer,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50)
    shop_logo = models.ImageField(blank=True,upload_to='shop_images')
    description = models.TextField(max_length=200,null=True,blank=True)
    shop_address = models.CharField(max_length=200)
    owner = models.CharField(max_length=50)
    contact = models.CharField(max_length=13)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.shop_name




class Products(models.Model):
    shop = models.ForeignKey(AboutShop,on_delete=models.CASCADE)
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(blank=True,upload_to='products_images')
    type = models.CharField(max_length=50)
    weight = models.FloatField()
    description = models.TextField(null=True,blank=True)
    discount_price = models.FloatField(blank=True,null=True,default=0)
    available_no = models.IntegerField(null=True,blank=True)
    available_status = models.BooleanField(default=True)
    more_image1 = models.ImageField(null=True,blank=True)
    more_image2 = models.ImageField(null=True,blank=True)
    more_image3 = models.ImageField(null=True,blank=True)
    more_image4 = models.ImageField(null=True,blank=True)
    more_image5 = models.ImageField(null=True,blank=True)
    

    def __str__(self):
        return self.pname




class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered =models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.id)

    # @property
    # def get_cart_total(self):
    #     ordered_items = self.ordereditems_set.all()
    #     total = sum([item.get_total for item in ordered_items])
    #     return total
    
    # @property
    # def get_cart_items(self):
    #     ordered_items = self.ordereditems_set.all()
    #     total = sum([item.qty for item in ordered_items])
    #     return total




class OrderedItems(models.Model):
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    qty = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # @property
    # def get_total(self):
    #     if self.product.discount_price == 0:
    #         total = self.product.price * self.qty
    #     else:
    #         total = self.product.discount_price * self.qty

    #     return total

    


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    address = models.CharField(max_length=200,null=False)
    city = models.CharField(max_length=200,null=False)
    state = models.CharField(max_length=200,null=False)
    zipcode = models.CharField(max_length=200,null=False)
    date_added =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
