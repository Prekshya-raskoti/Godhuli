from django.shortcuts import render
from django.urls import reverse_lazy

def about_view(request):
    return render(request, 'pages/about.html')