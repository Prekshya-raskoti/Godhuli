from django.shortcuts import render


def services_view(request):
    return render(request, 'pages/services.html')