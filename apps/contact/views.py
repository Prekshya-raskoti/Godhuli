from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm

# def home_view(request):
#     return render(request, 'pages/home.html')

# def about_view(request):
#     return render(request, 'pages/about.html')

def services_view(request):
    return render(request, 'pages/services.html')

def portfolio_view(request):
    return render(request, 'pages/portfolio.html')

def team_view(request):
    return render(request, 'pages/team.html') 

class ContactView(FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('pages:contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message has been sent successfully.")
        return super().form_valid(form)