from django.shortcuts import render, redirect
import os

def index(request):
    print(os.listdir('./apps/taco_montes_app/static/img'))
    picture = {
        "file_list": os.listdir('./apps/taco_montes_app/static/img'),
        "key": 'KEY'
    }
    return render(request, "index.html", picture)
