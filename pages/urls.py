from django.urls import path
from pages import views
from .views import ContactView

app_name = 'pages'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('team/', views.team_view, name='team'), 
    path('contact/', ContactView.as_view(), name='contact'),
]
