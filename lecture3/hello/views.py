from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")


def dipu(request):
    return HttpResponse("Hello Dipu")


def ramiza(request):
    return HttpResponse("Hello Ramiza")


def greating(request, name):
    return HttpResponse(f"Hello {name.capitalize()}")
