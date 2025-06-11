from django.views.generic import TemplateView
from apps.home.models import Homepage

class HomepageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homepage'] = Homepage.objects.first()  # assuming only one instance
        return context
