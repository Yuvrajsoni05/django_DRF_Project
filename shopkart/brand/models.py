from django.db import models

# Create your models here.
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    website = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='brands_logo/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.brand_name
    