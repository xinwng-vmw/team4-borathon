from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':  # user requesting data
        snippets = Transaction.objects.all()
        serializer = TransactionSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # user posting data
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return HttpResponse("Transactions index")
