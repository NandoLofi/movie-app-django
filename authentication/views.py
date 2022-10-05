from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.
def register(request):
    if request.method == "Post":
        user = User.objects.create_user(email=request.POST["email"], password=request.POST["passwrod"])
        
        login(request, user)
        return HttpResponse("success")
    
    else:
        return render(request, "authentication/register.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
        else:
            return redirect("/")
    else:
        return render(request, "authentication/login.html")