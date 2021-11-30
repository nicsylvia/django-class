from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'public/index.html')

def about(request):
     return render(request, 'public/about.html')

def rent(request):
     return render(request, 'public/rent.html')

def add_location(request):
     return render(request, 'public/add-location.html')

def dashboard(request):
     return render(request, 'public/dashboard.html')

