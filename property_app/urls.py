from django.urls import path, include
from property_app import views

app_name = 'property_app'

urlpatterns = [
    path('add-location/', views.add_location, name ='add_location'),
    path('', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('about-detail/<int:abt>', views.about_detail, name='about_detail'),
    path('property-detail/<slug:silver_slug>', views.property_detail, name='property_detail'),
    path('property-type/<slug:slug>', views.properties_from_property_type, name='property_type_url'),
    # property_type_url this must be the same with the href on the template.
    path('login-page/', views.login_view, name='site_login_view'),
    path('logout-page/', views.logout_view, name='logout_view'),
]
