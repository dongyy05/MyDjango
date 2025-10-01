from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("THis is userIndex")

def login(request):
    return HttpResponse("This is userLogin")
# Create your views here.
