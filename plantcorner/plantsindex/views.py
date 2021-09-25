from django.contrib.auth.decorators import login_required
from os import path
from fetch import get_data
from django.shortcuts import render
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

# from django.
# Create your views here.


@login_required
def index(request):
    context = {
        'data': get_data()
    }
    return render(request, 'plants.html', context=context)


def home(request):
    return render(request, 'home.html')


@login_required
def uploads(request):
    return render(request, 'upload.html')


@login_required
def weather(request):
    return render(request, 'weather.html')
