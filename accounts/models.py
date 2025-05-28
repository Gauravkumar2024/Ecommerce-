import uuid
from django.db import models
from django.contrib.auth.models import User
from base.models import baseModel
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from base.utils import send_verification_email  # Import the function from utils.py
from products.models import products,Colors_type,Size_type,product_image

class profile(baseModel):
    name=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_verify=models.BooleanField(default=False)
    mail_token=models.CharField(max_length=100, null=True, blank=True)
    profile_img=models.ImageField(upload_to="profile")
# Create your models here.

    # def Counter(self):
    #     return CartItem.objects.filter(user=self.user).count()
    
@receiver(post_save, sender=User)

def create_profile(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            profile.objects.create(name=instance, mail_token=email_token)
            # mail=instance.email
            send_verification_email(instance.email, email_token)
    except Exception as e:
        print(e)

class Cart(baseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="carts")
    is_paid=models.BooleanField(default=False)


    def __str__(self):
        # Display cart with user and whether it's paid, and number of items in the cart
        cart_items_count = self.cartitem_set.count()  # Count how many items are in the cart
        return f"Cart for {self.user.username} (Items: {cart_items_count}, Paid: {self.is_paid})"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # Reference to Cart model
    product = models.ForeignKey(products, on_delete=models.SET_NULL, null=True)  # Allow null if product is deleted
    color = models.ForeignKey(Colors_type, on_delete=models.SET_NULL, null=True)  # Allow null if color is deleted
    size = models.ForeignKey(Size_type, on_delete=models.SET_NULL, null=True)  # Allow null if size is deleted
    price_new = models.IntegerField(default=0)
    image = models.ForeignKey(product_image, on_delete=models.SET_NULL, null=True, blank=True)  # Add thi


    def __str__(self):
      # Show product name, size, and color (if any) in a user-friendly format
        size_str = f"Size: {self.size.size_number}" if self.size else "Size: Not selected"
        color_str = f"Color: {self.color.color_name}" if self.color else "Color: Not selected"
        return f"Product: {self.product.product_name} ({size_str}, {color_str})"
    
    def Counter(request):
       return CartItem.objects.count()
