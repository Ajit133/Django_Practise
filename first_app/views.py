from multiprocessing import context
from operator import index
import re
from turtle import update
from unicodedata import name
from urllib import request
from django import views
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Student,Student_info
from first_app import forms

def index(request):
    student_list = Student.objects.order_by('first_name')
    diction = {"student":student_list}
    return render(request,'index.html',context=diction)

def form(request):
    new_form = forms.StudentForm()
    
    
    if request.method == "POST":
        new_form = forms.MusicianForm(request.POST)
        # diction.update({"test_form": new_form})
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    diction = {"test_form":new_form}
    return render(request,"form.html",context=diction)
