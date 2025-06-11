from django.shortcuts import render

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def services_view(request):
    return render(request, 'pages/services.html')

def portfolio_view(request):
    return render(request, 'pages/portfolio.html')

def team_view(request):
    return render(request, 'pages/team.html')  

def contact_view(request):
    return render(request, 'pages/contact.html')
