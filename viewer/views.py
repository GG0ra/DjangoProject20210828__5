from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from viewer.models import Movie
# Create your views here.


class MoviesView(View):
    def get(self, request):
        return render(
            request, template_name='movies.html',
            context = {
                'movies': Movie.objects.all()
            }
        )
