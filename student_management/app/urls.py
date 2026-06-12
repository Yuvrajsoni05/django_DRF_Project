from django.contrib import admin
from django.urls import path,include
from .views import StudentAPIView,StudentDetailView ,StudentListGenericAPIView,StudentListGenericDetailView,StudentMixinAPIView,StudentMixinDetailView,StudentListAPIView,StudentDetailAPIView,StudentViewSetAPIView,StudentListGenericFilterAPIView,StudentListGenericSearchFilterAPIView,DepartmentViewSet,StudentNestedSerilizerViewSetAPIView,DepartmentNestedSerilizerViewSetAPIView,CourseViewSetAPIView,StudentWritableViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('student_writable',StudentWritableViewSet,basename='student_writable'
)
router.register('department_nested_serializer',DepartmentNestedSerilizerViewSetAPIView,basename='department_nested_serializer')

router.register('course_serializer',CourseViewSetAPIView,basename='course_serializer')

router.register('nested_serializer',StudentNestedSerilizerViewSetAPIView,basename='student_nested_serializer')

router.register('students',StudentViewSetAPIView,basename='student')

router.register('departments',DepartmentViewSet,basename='department')

department_list =  DepartmentViewSet.as_view(
    {
        'get':'list',
        'post':'create'
    }
)

# department_detail =  DepartmentViewSet.as_view(
#     {
#         'get':'retrieve',
#         'put':'update',
#         'patch':'partial_update',
#         'delete':'destroy'
#     }
# )




student_list = StudentViewSetAPIView.as_view(
    {
        'get':'list',
        'post':'create'

    }
)
student_detial = StudentViewSetAPIView.as_view(
    {
        'get':'retrieve',
        'put':'update',
        'patch':'partial_update',
        'delete':'destroy'
    }
)




urlpatterns = [
    path('api/students/',StudentAPIView.as_view(),name='student-list'),
    path('api/students/<int:pk>/',StudentDetailView.as_view(),name='student-detail'),
    path('api/generic/students/',StudentListGenericAPIView.as_view(),name='student-genric-list'),
    path('api/generic/students/<int:pk>/',StudentListGenericDetailView.as_view(),name='student-genric-detail'),
    path('api/mixins/student',StudentMixinAPIView.as_view(),name='student-list-mixin'),
    path('api/mixins/student/<int:pk>/',StudentMixinDetailView.as_view(),name='student-detial-mixins'),
    path('api/student/concrete_generic_views',StudentListAPIView.as_view(),name="student_concrete_generic_views"),
    path('api/student/concrete_generic_views/<int:pk>/',StudentDetailAPIView.as_view(),name="student_concrete_generic_views-detail"),
    path('api/student/viewset_api',student_list,name='student_view_set'),
    path('api/student/viewset_api/<int:pk>/',student_detial,name='student_detail_viewset'),
    path('api/student/generic_filter_api/',StudentListGenericFilterAPIView.as_view(),name='student_list_generic_filter_api'),
    path('api/student/generic_search_filter/',StudentListGenericSearchFilterAPIView.as_view(),name='student_search_filter_api' ),
    path('api/v7/',include(router.urls)),


    # path('student_list/',student_list,name='student_list')
]