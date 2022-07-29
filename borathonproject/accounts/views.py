from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Account
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import AccountSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        accounts = Account.objects.all()

        data = JSONParser().parse(request)

        for d in data:
            print("DATA: " + d)
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
