from django.shortcuts import render
from .models import products
# Create your views here.

def home(request):
    return render(request, 'home.html')


def products(request):
    prod = products.objects.all()

    return render(request, "products.html",{'prod':prod}) 
  