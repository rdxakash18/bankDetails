from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import bankData

def index(request):

    return HttpResponse("Hello, world. You're at the smaple note index.")
