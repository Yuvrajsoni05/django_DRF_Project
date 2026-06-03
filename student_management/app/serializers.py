from rest_framework import serializers

from .models import Student

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




