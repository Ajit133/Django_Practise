from django import forms
from django.core import validators
from first_app import models
from django.forms import ModelForm
from first_app.models import Student,Student_info

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields ="__all__"