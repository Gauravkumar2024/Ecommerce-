from django.urls import path
from products.views import *
from uuid import UUID  # Import UUID

urlpatterns = [
   
    path('<slug>/', get_product , name="get_product"),
    path('add-to-cart/<uuid:id>/', add_to_cart, name='addTocart'),  # Accept UUIDs 
]