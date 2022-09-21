from http.client import HTTPResponse
import pstats
from django.shortcuts import render, redirect
import environ
env = environ.Env()
environ.Env.read_env()
from django.http import HttpResponse
import requests
from .models import Comment
from django.contrib.auth.models import User

API_KEY = env('API_KEY')
# Create your views here.
def search(request):
    query = request.GET.get ('q')
    results = []
    if query:
        data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
 
    return render(request, 'home/results.html', {
        "data": data.json(),
    })

def showdetail(request, id):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{id}?api_key={API_KEY}&language=en-US")

    return render(request, 'home/details.html', {
        "data": data.json()
    })

def comments(request, show_id):
    if request.method == "POST":
        user = request.user
        comment = request.POST.get("comment")

        if not request.user.is_authenticated:
            user = User.objects.get(id=1)

        Comment(comment=comment, user=user, show_id=show_id).save()

        return redirect(f"/show/{show_id}/comments/")
    else:
        data = requests.get(f"https://api.themoviedb.org/3/tv/{show_id}?api_key={API_KEY}&language=en-US")

        Comments = Comment.objects.filter(show_id=show_id)

        return render(request, "home/comments.html", {
            "data": data.json(),
            "Comments": Comments

        })

def index(request):
    return render(request, 'home/index.html')