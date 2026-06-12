from rest_framework import serializers

from .models import Student,Department,StudentProfile,Course

class StudentSerializer(serializers.ModelSerializer):
    # Model Serializer
    class Meta:
        model = Student
        fields = '__all__'



    # id = serializers.IntegerField(read_only=True)
    # student_name = serializers.CharField(max_length=100)
    # student_age = serializers.IntegerField()



    # def create(self,validated_data):
    #     return Student.objects.create(**validated_data)




class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'



class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentNestedSerializer(serializers.ModelSerializer):
    profile = StudentProfileSerializer(read_only=True
        
    )
    department = DepartmentSerializer(read_only=True)
    courses = CourseSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Student
        fields = [
        'id',
        'student_name',
        'student_age',
        'profile',
        'department',
        'courses'
        ]



class StudentWritableSerializer(serializers.ModelSerializer):
    profile = StudentProfileSerializer()
    class Meta:
        model = Student
        fields = [
            'id',
            'student_name',
            'student_age',
            'profile'
        ]
    def create(self,validated_data):
        profile_data =validated_data.pop(
            'profile'
        )
        student = Student.objects.create(
            **validated_data
        )
        StudentProfile.objects.create(
            student=student,
            **profile_data
        )
        return student


class DepartmentNestedSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = [
        'id',
        'department_name',
        'students'
        ]

    students =  StudentSerializer(many=True)



