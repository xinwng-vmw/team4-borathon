from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AccountSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request == 'GET':
        snippets = Account.objects.all()
        serializer = AccountSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)