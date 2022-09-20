from http.client import HTTPResponse
from django.shortcuts import render
import environ
env = environ.Env()
environ.Env.read_env()
from django.http import HttpResponse
import requests

API_KEY = env('API_KEY')
# Create your views here.
def search(request):
    query = request.GET.get ('q')
    results = []
    if query:
        data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
 
    return render(request, 'home/results.html', {
        "data": data.json(),
        "type": request.GET.get("type")
    })

def moviedetail(request):
    return render(request, 'home/details.html')

def index(request):
    return render(request, 'home/index.html')