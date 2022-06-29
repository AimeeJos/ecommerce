from django.urls import path
from . import views


urlpatterns = [
   
    path('',views.home, name='home'),
    path('register/',views.register,name='register'),
    path('shops/',views.allshops,name='shops'),
    path('details/',views.product_details,name='product_details'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
     path('shop_details/<int:id>',views.shop_details,name='shop_details'),
    

]