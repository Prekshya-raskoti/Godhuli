# apps/home/urls.py

from django.urls import path
from apps.home import views
from django.urls import path
from .views import single_page_view

app_name = 'home'

urlpatterns = [
    path('', single_page_view, name='home_page'),  # root points to single-page view
    
    path('', views.HomepageView.as_view(), name='home'),
]

