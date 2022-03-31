from django.shortcuts import render
from .models import Movie, Category, Actors
# Create your views here.
def category_detail(request, category_id):
    context = {
        'movies' : Movie.objects.filter(categories__id=category_id),
        'categories' : Category.objects.all()
    }
    return render(request, 'homepage.html', context)

def movieList(request):
    context = {
        'movies' : Movie.objects.all(),
        'categories' : Category.objects.all()
    }
    return render(request, 'homepage.html', context)
    
def actorList(request):
    context = {
        'actors' : Actors.objects.all(),
    }
    return render(request, 'actors.html', context)