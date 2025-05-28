from django.urls import path
from home.views import index,AboutUs, carts,removeCart
# from accounts.views import activate_mail
# from uuid import UUID  # Import UUID
urlpatterns = [
   
    path('', index , name="index"),
    path('about/', AboutUs , name="about"),
    path('carts/', carts ,name='cart' ),
    path('remove/<int:id>', removeCart ,name='remove' )
    
]