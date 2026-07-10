from django.db import models
import uuid
from brand.models import Brand
from categories.models import Category
# Create your models here.
class Product(models.Model):
    id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False
)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    sku = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,related_name="products")
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name="products")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    



class ProductImage(models.Model):
    id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False
)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"Image for {self.product.product_name}"
    