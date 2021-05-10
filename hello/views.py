from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse("Hello world")
def test2(requst):
    return HttpResponse("<h1>Heloooo</h1>")
def test3(request):
    return render(request,"index.html")