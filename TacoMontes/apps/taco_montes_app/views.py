from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager
from django.core.files.storage import FileSystemStorage
import os

def index(request):
    print(os.listdir('./apps/taco_montes_app/static/img'))
    picture = {
        "file_list": os.listdir('./apps/taco_montes_app/static/img'),
        "key": 'KEY'
    }
    return render(request, "index.html", picture)

def showApp(request):
    return render(request, 'careers.html')


def career(request):
    print(request.method)
    print(request.FILES["myfile"])
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/showApp')
    else:
        if request.method == 'POST':
            file = request.FILES['myfile']
            fs = FileSystemStorage()
            fs.save(file.name, file)
            print(file.name)
            User.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                document = file,
            )
    return redirect('/career')