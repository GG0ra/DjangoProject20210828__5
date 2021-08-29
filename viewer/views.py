from django.shortcuts import render
from django.views.generic import TemplateView
from viewer.models import Movie

# Create your views here.


class MoviesView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.all()    }

