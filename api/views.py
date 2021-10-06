from django.db.models import manager
from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin

# for parsers
from rest_framework.parsers import FormParser, MultiPartParser

# import viewset
from rest_framework.viewsets import ModelViewSet
# Create your views here.


# In APIView we need to specify the get method, but in ListAPIView, we do not need to specify the 
# get method, we just need to put the queryset (means you need to mention the model name that you  need to query)
# and serializer_class (means you need to mention the serializer name to serialize the data)
class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


'''
note:
updateapiview will allow both PUT and PATCH request.
PUT: you have to provide full body info of the object, then you can specify which
value you need to update
PATCH: better than PUT bcoz you just need to give the value to update of the object

to create url you need to provide the object id number.
such as: api/products/update/<id of product>/

'''

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'