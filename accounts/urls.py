from django.urls import path
from accounts.views import *
# from accounts.views import activate_mail

urlpatterns = [
   
    path('login', login_req , name="login"),
    path('reg', register_page , name="reg"),
    path('activate/<str:token>/', activate_mail, name="activate_mail"),
]