from django.db import models
import uuid
from Accounts.models import User
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    category_name       = models.CharField(max_length=100)
    slug                = models.SlugField(unique=True, null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.category_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)+'-'+ str(uuid.uuid4())
        
        return super(Category, self).save(*args, **kwargs)


class ColorImage(models.Model):
    image = models.ImageField(upload_to='product-color-image')
    
    def __str__(self) -> str:
        return self.image.name
    

class Product(models.Model):
    product_name         = models.CharField(max_length=260)
    product_code         = models.CharField(max_length=20)
    product_quintity     = models.IntegerField(default=0)
    product_category     = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    roduct_title         = models.CharField(max_length=260)
    image                = models.ImageField(upload_to='products')
    product_color_image  = models.ManyToManyField(ColorImage, blank=True, null=True, related_name="colorImg")
    color_name           = models.CharField(max_length=160)
    slug                 = models.SlugField(unique=True, null=True, blank=True)
    details              = models.TextField()
    main_price           = models.IntegerField()
    is_newarival         = models.BooleanField(default=False)
    is_discount          = models.BooleanField(default=False)
    dic_price            = models.IntegerField(default=0, blank=True, null=True)
    cerated_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.product_name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.roduct_title)+'-'+ str(uuid.uuid4())
        
        return super(Product, self).save(*args, **kwargs)
    
    

    
  
  
class WishList(models.Model):
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return str(self.user.email) +'==>'+str(self.product.product_name)
    


