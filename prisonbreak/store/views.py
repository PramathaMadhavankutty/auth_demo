from django.shortcuts import render
from .models import Item


def index(request):
    return render(request, 'template.html')


def store(request):
    count = Item.objects.all().count()
    context = {
        'count': count
    }
    return render(request, 'store.html', context)
