from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm

class ContactView(FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('pages:contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message has been sent successfully.")
        return super().form_valid(form)