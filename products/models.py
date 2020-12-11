from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator

class Product(models.Model):

    title = models.CharField( max_length = 100, blank = True)
    price = models.IntegerField(
        validators=[
        MaxValueValidator(100000) ,
        MinValueValidator(10)],
        blank = False ,
        null = False ,
        default= 0,
    )
    description = models.TextField(blank= True) 
    image = models.ImageField(upload_to = 'media/products' , blank = True , null = True)

    def __str__(self):
        return self.title
    