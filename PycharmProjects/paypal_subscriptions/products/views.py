from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html",{"products":products})
def get_index(request):
    return render(request, "home.html")