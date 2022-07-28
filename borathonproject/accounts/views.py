from django.shortcuts import render
from django.http import HttpResponse
from .models import Account

# Create your views here.
def index(request):
    return HttpResponse("You're currently at the accounts view!")