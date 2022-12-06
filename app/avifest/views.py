from django.shortcuts import render
from django.http import HttpRequest
from utils import get_db_handle


def index(request: HttpRequest):
    return render(request, 'index.html', context={})

def login(request: HttpRequest):
    if request.method == 'POST':
        print(request.POST)
        
    return render(request, 'login.html', context={})

def register(request: HttpRequest):
    if request.method == 'POST':
        print(request.POST)

def home(request: HttpRequest):
    return render(request, 'home.html', context={'navbar': True})

def programme(request: HttpRequest):
    db = get_db_handle()
    artist_collection = db['artists']
    category_collection = db['category']
    artists = artist_collection.find()
    categories = category_collection.find()
    
    return render(request, 'programme.html', context={'navbar': True, 'artists': artists, 'categories': categories})

def festival(request: HttpRequest):
    return render(request, 'festival.html', context={'navbar': True})


