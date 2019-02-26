from django.shortcuts import render, redirect
import os

def index(request):
    print(os.listdir('./apps/taco_montes_app/static/img'))
    picture = {
        "file_list": os.listdir('./apps/taco_montes_app/static/img'),
        "key": 'AIzaSyDDgOIrhEpeT1dcsMxvWOUSP25Izv5J1zA'
    }
    return render(request, "index.html", picture)
