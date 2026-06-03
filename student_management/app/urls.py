from django.contrib import admin
from django.urls import path
from .views import StudentAPIView,StudentDetailView ,StudentListGenericAPIView,StudentListGenericDetailView,StudentMixinAPIView,StudentMixinDetailView


urlpatterns = [
    path('api/students/',StudentAPIView.as_view(),name='student-list'),
    path('api/students/<int:pk>/',StudentDetailView.as_view(),name='student-detail'),
    path('api/generic/students',StudentListGenericAPIView.as_view(),name='student-genric-list'),
    path('api/generic/students/<int:pk>/',StudentListGenericDetailView.as_view(),name='student-genric-detail'),
    path('api/mixins/student',StudentMixinAPIView.as_view(),name='student-list-mixin'),
    path('api/mixins/student/<int:pk>/',StudentMixinDetailView.as_view(),name='student-detial-mixins')

    # path('student_list/',student_list,name='student_list')
]