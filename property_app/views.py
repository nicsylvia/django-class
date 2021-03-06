from django.shortcuts import render, redirect
from django.http import HttpResponse
from property_app.models import *
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
     rent = Property.objects.filter(offer_type= 'Rent').order_by('-created')[:3]
     sale = Property.objects.filter(offer_type= 'Sale').order_by('-created')[:3]
     context = {
          'rent_key': rent,
          'sale_key': sale,
     }
     return render(request, 'public/index.html', context)

def about(request):
     team = Team.objects.all()
     return render(request, 'public/about.html', {'team': team})

def about_detail(request, abt):
     team_detail = Team.objects.get(id=abt)
     return render(request, 'public/about-detail.html', {'detail': team_detail})

def property_detail(request, silver_slug):
     detail_property = Property.objects.get(slug=silver_slug)
     if request.method == 'POST':
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          message = request.POST.get('message')
          get_property = Property.objects.get(slug=silver_slug)
          get_user = get_property.agent_id
          submit_data = ContactAgent(name=name, email=email, phone=phone, property_id=get_property, agent_id=get_user,message=message)
          submit_data.save()
          messages.success(request, 'Message sent Successfully')
     return render(request, 'public/property-details.html', {'detail':detail_property})

def properties_from_property_type(request, slug):
     property_type = Property.objects.filter(property_type__slug=slug).order_by('-created')
     return render(request, 'public/property_type.html', {'property_type':property_type})
     
def rent(request):
     return render(request, 'public/rent.html')

def add_location(request):
     return render(request, 'public/add-location.html')

@login_required(login_url='/frontend-pages/login-page/')
def dashboard(request):
     return render(request, 'public/dashboard.html')

def login_view(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request, user)
               return redirect('property_app:dashboard')
          else:
               return messages.error(request, 'Username and password do not match')
     return render(request, 'public/login.html')

def logout_view(request):
     logout(request)
     return redirect('property_app:site_login_view')




