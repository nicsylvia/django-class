from django.urls import path
from dashboard_app import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.dashboard, name= 'dashboard'),
]