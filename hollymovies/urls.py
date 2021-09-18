"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import MoviesView, MovieCreateView, \
    MovieUpdateView, MovieDeleteView, MovieDetailView
from viewer.models import Genre, Movie

from viewer.views import generate_demo

from accounts.views import SubmittableLoginView, SubmittablePasswordChangeForm,\
    SignUpView  # <== TUTAJ NOWE

from django.contrib.auth import views

from viewer.admin import MovieAdmin

# admin.site.register(Genre)
# admin.site.register(Movie)
admin.site.register(Movie, MovieAdmin)


urlpatterns = [
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', SubmittablePasswordChangeForm.as_view(),
         name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done', views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('sign-up/', SignUpView.as_view(), name='sign_up'), # <=== TUTAJ NOWE

    path('admin/', admin.site.urls),
    path('', MoviesView.as_view(), name='index'),
    path('demo', generate_demo, name='demo'),
    path('movie/create', MovieCreateView.as_view(), name='movie_create'),
    path('movie/details/<id>', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),
]
