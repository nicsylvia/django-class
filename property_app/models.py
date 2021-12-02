from django.db import models
from django.contrib.auth.models import User
# this:(django.contrib.auth.models) is in your project.

# Create your models here.
# they were all taken from the datebase we did on property listing website.
class Location(models.Model):
    location_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

class OfferType(models.Model):
    offer_type_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

class PropertyType(models.Model):
    property_type_name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)

class property(models.Model):
    property_name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    offer_type_id = models.ForeignKey(OfferType,  on_delete=models.CASCADE)
    agent_id = models.ForeignKey(User,  on_delete=models.CASCADE)
    image1 = models.FileField(blank=True, null=True, upload_to='uploads/')
    image2 = models.FileField(blank=True, null=True, upload_to='uploads/')
    image3 = models.FileField(blank=True, null=True, upload_to='uploads/')
    description = models.TextField()
    address = models.TextField()
#  on_delete=models.CASCADE means if idelete a particular location or something everything under it will be deleted
class ContactAgent(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    property_id = models.ForeignKey(property, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    message = models.TextField()
