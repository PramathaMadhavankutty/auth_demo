from django.shortcuts import render

def index(request):
    return render(request, 'template.html')


def home(request):
    return render(request, 'home.html')