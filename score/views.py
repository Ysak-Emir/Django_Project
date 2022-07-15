from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def homepage(request):
    return HttpResponse("Домашняя страница")

def Axe(request):
    axe_object = Product.objects.get(id=1)
    description = axe_object.description
    return HttpResponse(description)

def categories(request):
    return HttpResponse("Категории")