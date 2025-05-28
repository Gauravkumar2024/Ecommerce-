from django.contrib import admin
from .models import *
admin.site.register(category)

admin.site.register(product_image)
# Register your models here.

class productImageAdmin(admin.StackedInline):
    model=product_image
    #ye tabhi chalrga
   # extra = 1  # Kitne extra empty forms dikhen (default: 3) admin panel me 
class productAdmin(admin.ModelAdmin):
    list_display=['product_name','category','price']
    inlines=[productImageAdmin] # Product ke andar Image form dikhega

admin.site.register(products,productAdmin) #rpduct admin me product_image view ko display krwa diya hai

#agr modeladmin ke bare me detail janai hai to ecom hepler folder me jao waha hai sctackinded vs modeladmin
@admin.register(Colors_type)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display=['color_name','new_price']
    # model=Colors_type

@admin.register(Size_type)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display=['size_number','new_price2']
    # model=Size_type
