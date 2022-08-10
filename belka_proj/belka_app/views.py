from django.shortcuts import render
from belka_app.models import Photo

def index(request):
    photos = Photo.objects.all()
    photos_dict = {'photos': photos}
    return render(request, 'index.html', context=photos_dict)

def about(request):
    return render(request, 'about me.html', context={})