from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def disc(request):
    return HttpResponse("hello world")

def contact(request):
    return HttpResponse("contact")
