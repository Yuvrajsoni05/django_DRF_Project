from django.contrib import admin
from django.urls import path, include
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='product')

product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', product_list, name='product-list'),
    path('<int:pk>/', product_detail, name='product-detail'),
    
    

]