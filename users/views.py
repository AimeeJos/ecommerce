from django.http import HttpResponse
from django.shortcuts import render
from shops.models import *

def home(request):
    products = Products.objects.all()
    context={'products':products}

    return render(request,'./home/home.html',context)

def register(request):
    return render(request,'./home/register.html')

def allshops(request):
    shops = AboutShop.objects.all()
    context={'shops':shops}

    return render(request,'./home/shops.html',context)

def shop_details(request,id):
    details = AboutShop.objects.get(shop_id=id)
    products = Products.objects.filter(shop_id=id)
    

    context={'details':details,'products':products}

    return render(request,'./home/shop_details.html',context)

def product_details(request):
    return render(request,'./home/product_details.html')

def cart(request):
    return render(request,'./home/cart.html')

def checkout(request):
    return render(request,'./home/checkout.html')

        