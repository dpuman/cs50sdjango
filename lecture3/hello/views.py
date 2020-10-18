from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'hello/index.html')


def dipu(request):
    return HttpResponse("Hello Dipu")


def ramiza(request):
    return HttpResponse("Hello Ramiza")


def greating(request, name):
    return render(request, 'hello/greet.html', {'name': name.capitalize()})
