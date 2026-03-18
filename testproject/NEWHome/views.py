from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hey(request):
    fst="<h1>hello welcome back</h1>"
    return HttpResponse(hey)


def wow(request):
    return render (request,'one.html')