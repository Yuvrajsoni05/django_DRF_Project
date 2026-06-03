from django.shortcuts import render
from .models import Student
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
)
# Create your views here.

class StudentAPIView(APIView):
    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors)



class StudentDetailView(APIView):
    def get(self,request,pk):
        student = get_object_or_404(
            Student,
            pk=pk
        )
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,pk):
        student = get_object_or_404(Student,pk=pk)
        serializer = StudentSerializer(
            instance=student,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self,request,pk):
        student = get_object_or_404(
            Student,pk=pk
        )

        serializer = StudentSerializer(
            instance =student,
            data = request.data,
            partial=True

        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(safe,request,pk):
        student = get_object_or_404(
            Student,pk=pk
        )
        student.delete()
        return Response(
            {
                "message":"Student Delete Successfully"
            }
        )

class StudentListGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request):
        student = self.get_queryset()
        serializer = self.get_serializer(
            student,
            many=True
        )
        return Response(serializer.data)
        
        
    def post(self,request):
        serializer = self.get_serializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    


class StudentListGenericDetailView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,pk):
        student = self.get_object()
        serializer =self.get_serializer(student)
        return Response(serializer.data)
    def put(self, request, pk):
        student = self.get_object()
        serializer = self.get_serializer(
            student,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self,request,pk):
        student =self.get_object()
        serializer =self.get_serializer(
            student,data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):

        student = self.get_object()

        student.delete()

        return Response({
            "message": "Student deleted successfully"
        })


class StudentMixinAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class StudentMixinDetailView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get(self,request,pk):
        return self.retrieve(request,pk=pk)
    def put(self,request,pk):
        return self.update(request,pk=pk)
    def patch(self,request,pk):
        return self.partial_update(request,pk=pk)
    def delete(self,request,pk):
        
        self.destroy(request,pk=pk)
        return Response({
            "message":"Delete Successfully"
        })



























# def student_list(request):
#     students = Student.objects.all()
#     data = []
#     for student in students:
#         data.append({
#             "id":student.id,
#             "student_name":student.student_name,
#             "student_age":student.student_age,
#         })
#     return JsonResponse(data,safe=False)