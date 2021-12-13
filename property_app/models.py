from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# this:(django.contrib.auth.models) is in your project.

# Create your models here.
# they were all taken from the datebase we did on property listing website.
class Location(models.Model):
    location_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.location_name

    class Meta():
        verbose_name_plural = 'LOCATION'
        #  verbose_name_plural = 'LOCATION' is for changing the name on your admin page

class PropertyType(models.Model):
    property_type_name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.property_type_name
        # def __str__(self):
        # return self.offer_type_name this makes the name to be descriptive like it shows the name you put there and not object 1.

    def get_property_type(self):
        return reverse('property_app:property_type_url', kwargs={'slug':self.slug})
        # property_type_url thisnis from the name on the url.

class Property(models.Model):
    RENT = 'Rent'
    SALE = 'Sale'
    CHOOSE = ''
    OFFER_TYPE = [
        ( RENT, 'Rent'),
        ( SALE, 'Sale'),
        (CHOOSE, 'please choose'),
    ]
    property_name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    property_type= models.ForeignKey(PropertyType,  on_delete=models.CASCADE)
    offer_type = models.CharField( max_length=25,verbose_name='OFFER_TYPE',choices = OFFER_TYPE, default=CHOOSE)
    agent_id = models.ForeignKey(User,  on_delete=models.CASCADE)
    image1 = models.FileField(blank=True, null=True, upload_to='uploads/')
    image2 = models.FileField(blank=True, null=True, upload_to='uploads/')
    image3 = models.FileField(blank=True, null=True, upload_to='uploads/')
    description = models.TextField()
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.property_name

    def get_img1(self):
        if self.image1:
            return self.image1.url

    def get_img2(self):
        if self.image2:
            return self.image2.url

    def get_img3(self):
         if self.image3:
             return self.image3.url
    
    def get_absolute_url(self):
        return reverse('property_app:property_detail', kwargs={'silver_slug':self.slug})

# with the above function it won't show up an error.

    class Meta():
        verbose_name_plural = 'property'
#  on_delete=models.CASCADE means if idelete a particular location or something everything under it will be deleted
class ContactAgent(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    message = models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    team_name = models.CharField (max_length=20)
    slug = models.SlugField(unique=True)
    profile = models.FileField(blank=True, null=True, upload_to='uploads/')
    designation = models.CharField(max_length=30)
    Biography = models.TextField()
   
    def __str__(self):
        return self.team_name

    class Meta():
        verbose_name_plural = 'Team'

    def get_profile(self):
        if self.profile:
            return self.profile.url

   