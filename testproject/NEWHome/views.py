from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hey(request):
    print("hello welcome back")
    fst="<h1>hello welcome back</h1>"
    # return render (request,'one.html')
    return HttpResponse(fst)


def wow(request):
    print("welcome to django")
    return render (request,'one.html')