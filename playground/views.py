from django.http import HttpResponse
from django.shortcuts import render

def caluclate():
    x = 1
    y = 10
    return y + x

def say_hello(request):
    x = caluclate()
    return render(request, 'hello.html', {'name': 'Django'})
