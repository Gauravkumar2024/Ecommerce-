from django.contrib import admin
from .models import profile,Cart,CartItem
# Register your models here.
admin.site.register(profile)
admin.site.register(Cart)
admin.site.register(CartItem)