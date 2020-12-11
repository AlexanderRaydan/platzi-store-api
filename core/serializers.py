#serealizador :
#database -> datos -> JSON
#JSON -> datos -> database

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['id' ,'title', 'price' , 'description' , 'image',]
        
