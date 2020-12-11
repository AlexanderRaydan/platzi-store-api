from django.contrib import admin

from .models import Product

# Register your models here.


@admin.register(Product)#registramos nuestro modelo de "Profile" en el sitio de admin
class ProductAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title', 'price' , 'description' , 'image') #como quiero que se listen las cosas en el admin
