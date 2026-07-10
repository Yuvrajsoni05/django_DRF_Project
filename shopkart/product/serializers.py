from rest_framework import serializers
from .models import Product,ProductImage







class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True) #images var is used to get all the images related to the product why images bcz it related name in the ProductImage model is images
    
    class Meta:
        model = Product
        fields = '__all__'