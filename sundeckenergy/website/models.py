from django.db import models
from django.core.validators import RegexValidator
from django import forms
from datetime import datetime
#from django.utils import timezone
from pytz import timezone

class Customer(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobileNum = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    roofType = models.CharField(max_length = 50)
    roofHeight = models.CharField(max_length = 20)
    electricityBoard = models.CharField(max_length = 100)
    otherDetails = models.TextField(max_length = 2000)
    address = models.CharField(max_length = 300)
    latitude = models.CharField(max_length = 30)
    longitude = models.CharField(max_length = 30)
    create_tmp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        create_tmp = self.create_tmp.astimezone(timezone('Asia/Kolkata'))
        return self.name + " - " + create_tmp.strftime('%d/%b/%Y %I:%M:%S %p')
