from multiprocessing import context
from django.shortcuts import render
from shops.models import Products


def index(request):
    products = Products.objects.all()
    print(products)
    context = {'products': products}
    return render(request,'purchase/home.html',context)

def details(request,id):

    product_details = Products.objects.get(pid=id)
    context={'item':product_details}

    return  render(request,'purchase/item_details.html',context)




def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
        items = OrderedItems.objects.filter(order=order)
    else:
        items=[]
        order={
            'get_cart_total':0,
            'get_cart_items':0,
            }

    context={'items':items,'order':order}
    return render(request,'purchase/cart.html',context)


def checkout(request):
    context={}
    return render(request,'purchase/checkout.html',context)