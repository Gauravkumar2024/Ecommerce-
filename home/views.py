from django.http import HttpResponseRedirect
from django.shortcuts import render
from products.models import products
from accounts.models import Cart,CartItem
# Create your views here.

def index(request):

    context={
         "product":products.objects.all()
    }
    print(context)
# for pro in context:
#     print(f" product name: {pro.product_name}, Summary :{pro.product_desc}, Price :{pro.price},Slug is :{pro.slug}, Category:{pro.category}")
#     products_with_images = products.objects.all()  # Get all products
#     for product in products_with_images:
#      images = product.product_image.all()  # Get all related images
#      # print(f"Product: {product.product_name}")
#      for img in images:
#           print(f"Image URL: {img.image.url}")



    return render(request, "home/index.html" , context)

def AboutUs(request):

    return render(request,"home/about.html")



def carts(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    total_price = sum(item.price_new for item in cart_items)
    context={
        'cart':CartItem.objects.filter(cart__user=request.user),
        'total':total_price
    }
    
    print(total_price)

    return render(request,'Acc/cart.html',context)

def removeCart(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))