from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages 

# Create your views here.

def register_view(request):

    if request.method == "GET":
        return render(request, "registration/register.html")
    
    if request.method == "POST":
        user_data = request.POST
        username = user_data["username"]
        email = user_data["email"]
        password = user_data["password1"]
        cpassword = user_data["password2"]

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                print(request, "Username already exists")
            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.save()
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('home')

    return render(request, 'registration/register.html')




