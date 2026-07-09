from django.contrib import admin
from django.urls import path, include
from .views import BrandGenericAPIView

urlpatterns = [
    
    path('', BrandGenericAPIView.as_view(), name='brand-list'),
    

]