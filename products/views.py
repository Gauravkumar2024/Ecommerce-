from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import products,Size_type,Colors_type,product_image
from accounts.models import Cart,CartItem


# def updatePrice(data):
#     print('hi')
#     data =  Size_type.objects.get(size_number=data).new_price2
#     return data

def get_product(request, slug):
    try:
       product_data=products.objects.get(slug=slug)
       context = {}
       if request.GET.get('size'):
           size=request.GET.get('size')
           print("size",size)
           price=product_data.price+Size_type.objects.get(size_number=size).new_price2
           print('rupey',price)
           context={
               'price':price,
               'size':size
           }
           
       product = products.objects.first()  # Get any product
       print(product.size_var.all())  # Check how many sizes are related
 
       print('mydata',product_data)

       #jo slug passs kiya hai uska pura data milega isse isko print krwane per khali
       #product name mil rhai hai kui usi per click krke yaha aye hai 
       #agar pura data access krna hai to .lagakr karenge


    #    data = products.objects.filter(slug='denver-deodrant').values()
    #    print(list(data))
    #iske use se pura slug ka data hai wo print hoga

       return  render(request,'product/products.html',context={'product':product_data,'update':context})
    except Exception as e:
        print('error',e)
        return HttpResponse("Something went wrong!")


def add_to_cart(request, id):
   
    # print('size:',sizes)
    data=products.objects.get(id=id)
    sizes=request.GET.get('variant')
    price=request.GET.get('price')
    # sizes=sizes
    print('s:',sizes)
    print('sii:',price)
    if not sizes:
            return HttpResponse("Size variant is required", status=400)

        # Strip whitespace before performing the lookup
    sizes = sizes.strip() if sizes else None
    new_datas=Size_type.objects.get(size_number=sizes)
    print('new_data',new_datas)
    
    img = product_image.objects.filter(product=id).first()
    print('images',img.image)
    
    size_data,cart_data=Cart.objects.get_or_create(user=request.user,is_paid=False)
    cart_item_count = CartItem.objects.filter(cart=size_data).count()
    cartValuesSave=CartItem.objects.create(cart=size_data,product=data,size=new_datas,price_new=price,image=img)

    cartValuesSave.save()
        # Store the updated cart item count in the session so that it can be used in the navbar
    request.session['cart_item_count'] = cart_item_count
    # print(data.id, sizes)
   #  cart_item, created = Cart.objects.get_or_create(is_paid=False, user=request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    # Optionally, add cart item count to session or context for the navbar
    # To display the updated count, you can store the count in the session for reuse

