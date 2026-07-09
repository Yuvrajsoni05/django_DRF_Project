from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializer import BrandSerializer
from .models import Brand
# Create your views here.


class BrandGenericAPIView(GenericAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    def get(self, request):
        brands =  self.get_queryset()
        serializer = self.get_serializer(brands, many=True)
        return Response({"message": "List of brands", "brands": serializer.data})
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Brand created"})
        else:
            return Response(serializer.errors, status=400)
    
    