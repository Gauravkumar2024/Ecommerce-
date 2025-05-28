from django.db import models
from base.models import baseModel
from django.utils.text import slugify  #import slug slug mean like "shoe-black-color" in url 

class category(baseModel):
    catagory_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True ,null=True, blank=True)
    category_image=models.ImageField(upload_to="categories")


    def save(self, *args, **kwargs):
        self.slug=slugify(self.catagory_name) ## Generate a slug based on category_name
        super().save(*args, **kwargs) ## Call the original save method

    # self: Refers to the instance of the model (in this case, a Category object).
    # *args: This allows you to pass any number of positional arguments to the method.
    # **kwargs: This allows you to pass any number of keyword arguments to the method.
    # These *args and **kwargs allow you to call the save() method with flexibility, and it ensures
    # slugify(self.category_name): This function from django.utils.text converts the category_name into a valid slug:
    # It transforms spaces into hyphens (" " → "-").
    # It converts all characters to lowercase.
    # It removes non-alphanumeric characters, making the slug URL-friendly.




    def __str__(self):
        return self.catagory_name

class Colors_type(baseModel):
    color_name=models.CharField(max_length=100)
    new_price=models.IntegerField(default=0)
    
    def __str__(self):
        return self.color_name

class Size_type(baseModel):
    size_number=models.CharField(max_length=100)
    new_price2=models.IntegerField(default=0)
    
    def __str__(self):
        return self.size_number

class products(baseModel):
    product_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True ,null=True, blank=True)
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name="products")
    price=models.IntegerField()
    product_desc=models.TextField()
    color_var=models.ManyToManyField(Colors_type, blank=True)
    size_var=models.ManyToManyField(Size_type, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.product_name) ## Generate a slug based on category_name
        super().save(*args, **kwargs) ## Call the original save method

    def __str__(self):
        return self.product_name

class product_image(baseModel):
    product=models.ForeignKey(products, on_delete=models.CASCADE, related_name="product_image")
    image=models.ImageField(upload_to="products")

