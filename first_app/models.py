from tkinter import CASCADE
from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    dept = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Student_info(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    S_fatherName = models.CharField(max_length=30)
    S_motherName = models.CharField(max_length=30)
    S_Permanent_address = models.CharField(max_length=30)

    def __str__(self):
        return self.S_fatherName + "Permanent Address is: " + self.S_Permanent_address

