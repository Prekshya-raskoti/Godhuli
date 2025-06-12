from django.shortcuts import render
from  apps.portfolio.models import Portfolio

def portfolio_view(request):
    items = Portfolio.objects.all()
    return render(request, 'pages/portfolio.html', {'items': items})
