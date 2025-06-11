# apps/home/urls.py

from django.urls import path
from apps.home import views

app_name = 'home'

urlpatterns = [
    
    path('', views.HomepageView.as_view(), name='home'),
]
