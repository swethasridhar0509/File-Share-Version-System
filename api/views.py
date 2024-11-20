from django.shortcuts import render 
from django.http import HttpResponse 

def home_view(request):
    return HttpResponse('<h1>HOME PAGE</h1>')

def file_view(request, id):
    print("file id - ", id)
    return HttpResponse('<h1>DETAILS PAGE</h1>')

def share_view(request, id):
    print("file share id - ", id)
    return HttpResponse('<h1>SHARE PAGE</h1>')