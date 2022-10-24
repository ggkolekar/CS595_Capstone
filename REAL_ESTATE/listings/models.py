from asyncio.windows_events import NULL
from ctypes import addressof
from datetime import datetime
from email.mime import image
from turtle import title
from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'
    
    class HomeType(models.TextChoices):
        HOUSE = 'House'
        CONDO = 'Condo'
        TOWNHOUSE = 'Townhouse'
    
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default= 'Not_Available')
    state = models.CharField(max_length=100, default= 'Not_Available')
    zipcode = models.CharField(max_length=15, default= 'Not_Available')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    square_footage = models.IntegerField()
    lot_size = models.DecimalField(max_digits = 5, decimal_places=1,default=1.0)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    home_type = models.CharField(max_length=50, choices=HomeType.choices, default=HomeType.HOUSE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published=models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    #image
    
    
    def __str__(self):
        return self.title
    

    

