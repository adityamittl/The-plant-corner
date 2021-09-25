from pathlib import Path
from .util import classify_image
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from os import path
from fetch import get_data
from django.shortcuts import render
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
BASE_DIR = Path(__file__).resolve().parent.parent


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
    if request.method == 'POST':
        if request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage(location='media/model')
            filename = fs.save(myfile.name, myfile)
            print(str(BASE_DIR)+'/media/model/'+filename)
            data = classify_image(str(BASE_DIR)+'/media/model/'+filename)
            typ = data['class']
            acc = data['class_probability']
            context = {
                'type': typ,
                'accuracy': acc,
                'result': True
            }
            return render(request, 'upload.html', context=context)

    return render(request, 'upload.html')


@login_required
def weather(request):
    return render(request, 'weather.html')
