from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserDetail(AbstractUser):
    ROLE_CHOICES = (
    ('customer', 'Customer'),
    ('seller', 'Seller'),
    ('admin', 'Admin'),
)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,unique=True,blank=True,null=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=50,choices=ROLE_CHOICES,default='customer')
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.username