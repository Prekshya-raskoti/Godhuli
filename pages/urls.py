from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('team/', views.team_view, name='team'), 
    path('contact/', views.contact_view, name='contact'),
]
