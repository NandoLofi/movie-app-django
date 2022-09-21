from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
# Create your views here.
def register(request):
    if request.method == "Post":
        user = User.objects.create_user(email=request.POST["email"], password=request.POST["passwrod"])
        
        login(request, user)
        return HTTPResponse("success")
    
    else:
        return render(request, "authentication/register.html")

def login_view()