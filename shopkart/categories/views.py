from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer
from django.shortcuts import get_object_or_404
from .models import Category
# Create your views here.



class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"message": "List of categories", "categories": serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Category created"})
        else:
            return Response(serializer.errors, status=400)



class CategoryDetail(APIView):
    def get(self, request, category_id):
        category_detail = get_object_or_404(Category, id=category_id)
        serializer = CategorySerializer(instance=category_detail)
        return Response({"message": f"Details of category", "category": serializer.data})
    def put(self, request, category_id):
        category_detail = get_object_or_404(Category, id=category_id)
        serializer = CategorySerializer(instance=category_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Category updated"})
        else:
            return Response(serializer.errors, status=400)
        
    def delete(self, request, category_id):
        category_detail = get_object_or_404(Category, id=category_id)
        category_detail.delete()
        return Response({"message": "Category deleted"})
    
        
        
       
    