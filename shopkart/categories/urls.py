from django.contrib import admin
from django.urls import path, include
from .views import CategoryAPIView, CategoryDetail

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:category_id>/',CategoryDetail.as_view(), name='category-detail'),
    

]
