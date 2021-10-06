'''
note: 
serializer will covert a model instance to a python dictionary.
so that we can get a json object from this.
'''

from django.db.models import fields
from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'