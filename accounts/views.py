from django.shortcuts import render

from django.views.generic import CreateView

from accounts.forms import (SignUpForm)

# Create your views here.

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy


class SubmittableLoginView(LoginView):
    template_name = 'form.html'


class SubmittablePasswordChangeForm(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('index')



class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')


