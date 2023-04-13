import email
from django.db import models
    
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Student(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, related_name="students", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



