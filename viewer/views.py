from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
import datetime # <=== ZMIANA

from viewer.models import Movie
from viewer.forms import MovieForm

from logging import getLogger
LOGGER = getLogger()

from django.contrib.auth.decorators import login_required # <=NOWE

from django.contrib.auth.mixins import LoginRequiredMixin

@login_required # <=NOWE
def generate_demo(request):
    our_get = request.GET.get('name', '')
    return render(
        request, template_name='demo.html',
        context={'our_get': our_get,
                 'list': ['pierwszy', 'drugi', 'trzeci', 'czwarty'],
                 'nasza_data': datetime.datetime.now() # <=== ZMIANA
                 }
    )


class MoviesView(LoginRequiredMixin, ListView):
    template_name = 'movies.html'
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    # adres pobrany z URLs na który zostaniemy przekierowani
    # gdy walidacja się powiedzie (movie_create pochodzi z name!)
    success_url = reverse_lazy('movie_create')

    # co ma się dziać, gdy formularz nie przejdzie walidacji:
    def form_invalid(self, form):
        # odkładamy w logach informacje o operacji
        LOGGER.warning('User provided invalid data')
        # zwracamy wynik działania pierwotnej funkcji form_invalid
        return super().form_invalid(form)

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = MovieForm
    # adres pobrany z URLs na który zostaniemy przekierowani
    # gdy aktualizacja się powiedzie (index pochodzi z name!)
    success_url = reverse_lazy('index')
    # Nazwa encji, z której będziemy aktualizować rekord
    model = Movie

    # co ma się dziać, gdy formularz nie przejdzie walidacji:
    def form_invalid(self, form):
        # odkładamy w logach informacje o operacji
        LOGGER.warning('User provided invalid data when updating')
        # zwracamy wynik działania pierwotnej funkcji form_invalid
        return super().form_invalid(form)

class MovieDeleteView(LoginRequiredMixin, DeleteView):
    #Nazwa szablonu wraz z rozszerzeniem którą pobieramy z folderu templates
    template_name = 'delete_movie.html'
    success_url = reverse_lazy('index')
    #Nazwa encji, z której będziemy kasować rekord
    model = Movie
