from django.shortcuts import render
from belka_app.models import Photo
from django.views.generic import ListView

# class PhotosView(ListView):
#     paginate_by = 2
#     model = Photo

def index(request):
    photos = Photo.objects.all().order_by('priority')
    count = 0
    column_1 = []
    column_2 = []
    column_3 = []

    for i in photos:
        if count > 2:
            count = 0
        if count == 0:
            column_1.append(i)
        elif count == 1:
            column_2.append(i)
        elif count == 2:
            column_3.append(i)
        count += 1

    context_photo_dict = {
        "column_1" : column_1,
        "column_2" : column_2,
        "column_3" : column_3
    }

    return render(request, 'index.html', context=context_photo_dict)

def postcards(request):
    return render(request, 'postcards.html', context={})

def about(request):
    return render(request, 'about me.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})
