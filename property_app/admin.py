from django.contrib import admin
from property_app.models import *
# * here represents all the models.
# this will make them show on your django admin page

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('location_name',)}


@admin.register(OfferType)
class OfferTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('offer_type_name',)}

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('property_type_name',)}

@admin.register(property)
class propertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('property_name',)}

admin.site.register(ContactAgent)
# the contact agent will be like this because it doesn't have slug.