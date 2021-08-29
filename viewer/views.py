from django.shortcuts import render
from django.views.generic import ListView
from viewer.models import Movie

# Create your views here.


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie
