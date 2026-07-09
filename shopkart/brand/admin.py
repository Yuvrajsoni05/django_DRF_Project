from django.contrib import admin
from .models import Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name', 'slug', 'description', 'logo', 'created_at', 'updated_at')
    
    search_fields = ('brand_name', 'slug', 'description')
    prepopulated_fields = {'slug': ('brand_name','id')}
