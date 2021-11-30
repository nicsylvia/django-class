from django.urls import path, include
from property_app import views

app_name = 'property_app'

urlpatterns = [
    path('add-location/', views.add_location, name ='add_location'),
    path('', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
]