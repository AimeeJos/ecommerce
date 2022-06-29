# from djongo import models
# from django.contrib.auth.models import User
# from shops.models import *


# class Customer(models.Model):
#     user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
#     name = models.CharField(max_length=50,null=True)
#     email = models.EmailField(max_length=200,null=True)

#     def __str__(self):
#         return self.name


# class Order(models.Model):
#     customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
#     date_ordered =models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=100,null=True)

#     def __str__(self):
#         return self.customer.name

#     @property
#     def get_cart_total(self):
#         ordered_items = self.ordereditems_set.all()
#         total = sum([item.get_total for item in ordered_items])
#         return total
    
#     @property
#     def get_cart_items(self):
#         ordered_items = self.ordereditems_set.all()
#         total = sum([item.qty for item in ordered_items])
#         return total




# class OrderedItems(models.Model):
#     product = models.ForeignKey(Products,on_delete=models.SET_NULL,blank=True,null=True)
#     order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
#     qty = models.IntegerField(default=0,null=True,blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     @property
#     def get_total(self):
#         if self.product.discount_price == 0:
#             total = self.product.price * self.qty
#         else:
#             total = self.product.discount_price * self.qty

#         return total

    


# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
#     order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
#     address = models.CharField(max_length=200,null=False)
#     city = models.CharField(max_length=200,null=False)
#     state = models.CharField(max_length=200,null=False)
#     zipcode = models.CharField(max_length=200,null=False)
#     date_added =models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.address
