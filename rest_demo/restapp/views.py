from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import book
# import viewsets
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
# import local data
from .serializers import bookSerializer


# create a viewset


class bookViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = book.objects.all()

    # specify serializer to be used
    serializer_class = bookSerializer

@api_view(['GET'])
def getData(request):
    app=book.objects.all()
    serializers=bookSerializer(app,many=True)
    return Response(serializers.data)
@api_view(['POST'])
def postData(request):
    serializer = bookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)        




# # Create your views here.
# @api_view(['GET'])
# def getFood(request):
#     return Response()
