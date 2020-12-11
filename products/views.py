from django.shortcuts import render , redirect
from django.views import generic
#models
from products.models import Product
from core.serializers import *

#restFramework
from rest_framework import viewsets
from core.serializers import serializers

from core.interseption import interception

class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers


@api_view(['GET'])
def funtion_test(request , id):

    product = Product.objects.get(pk = id)
    # print('++++++++++++')
    # print(str(product.image))    
    # print(type(product.image))
    # print('++++++++++++')
    name , percentage = interception(product)

    return Response({
        'name' : name,
        'porcentage': percentage
    })
      
