from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# /product -> index
def index(request):
    return HttpResponse("Hello World")


def new(request):
    return HttpResponse('New Product')
