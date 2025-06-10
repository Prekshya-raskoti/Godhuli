from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'service-details.html')

def portfolio_view(request):
    return render(request, 'portfolio-details.html')

def contact_view(request):
    return render(request, 'contact.html')
