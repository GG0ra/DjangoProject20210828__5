from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    s = request.GET.get('s', '')
    return render(
        request, template_name='hello.html', context={
            'adjectives': [s, 'beautiful', 'wonderful', 'cool']
        }
    )
