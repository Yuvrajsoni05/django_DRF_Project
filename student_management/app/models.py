from django.db import models

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.department_name

class Course(models.Model):

    course_name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_age = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True,related_name='students')
    courses = models.ManyToManyField(
        Course,
        related_name='students'
    )
    def __str__(self):
        return self.student_name


class StudentProfile(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE,related_name='profile')
    student_address = models.CharField(max_length=200,blank=True,null=True)
    student_phone = models.CharField(max_length=15,blank=True,null=True)
    
    