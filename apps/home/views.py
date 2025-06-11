from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

def home_view(request):
    return render(request, 'pages/home.html')
