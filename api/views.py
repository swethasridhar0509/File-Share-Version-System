from django.shortcuts import render 
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
 
@login_required(login_url='/login/')
def home_view(request):
    return render(request, 'api/home.html')

@login_required(login_url='/login/')
def file_view(request, id):
    print("file id - ", id)
    return render(request, 'api/detail.html')

@login_required(login_url='/login/')
def share_view(request, id):
    print("file share id - ", id)
    return render(request, 'api/share.html')