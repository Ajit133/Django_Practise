from urllib.parse import urlparse
from django.urls import re_path as url
from django.urls import path 
from first_app import views

app_name = "second_app"




urlpatterns = [
    path('',views.index,name='index'),
    path('form/',views.form,name='form')
]


