from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home Page')
def about(request):
    return HttpResponse('About Us')
def contact(request):
    return HttpResponse('Contact Us')
