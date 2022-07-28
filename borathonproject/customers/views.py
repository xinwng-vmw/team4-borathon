from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
def index(request):
    return HttpResponse("This is the customer view")

# Create your views here.
