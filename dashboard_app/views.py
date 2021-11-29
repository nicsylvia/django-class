from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('Login here 😉')
def dashboard(request):
    return HttpResponse('Dashboard Page 🤗')
