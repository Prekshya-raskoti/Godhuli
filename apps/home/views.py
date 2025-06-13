from django.views.generic import TemplateView
from apps.home.models import Homepage

from django.shortcuts import render
from apps.home.models import Homepage, SiteSetting
from apps.about.models import AboutSection, Testimonial
from apps.portfolio.models import Portfolio
from apps.team.models import TeamMember
from apps.contact.forms import ContactForm
from django.shortcuts import render
from apps.about.models import AboutSection, Testimonial
from apps.contact.forms import ContactForm
from apps.home.models import Homepage, SiteSetting, SocialLink
from apps.portfolio.models import Portfolio
from apps.team.models import TeamMember

def single_page_view(request):
    # Homepage Section
    homepage = Homepage.objects.first()
    site_settings = SiteSetting.objects.first()

    # About Section
    about = AboutSection.objects.prefetch_related('features').first()
    testimonials = Testimonial.objects.all()
    show_testimonial_loop = testimonials.count() > 2

    # Contact Form
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
    else:
        contact_form = ContactForm()

    # Portfolio & Team
    portfolios = Portfolio.objects.all()
    team_members = TeamMember.objects.all()

    return render(request, 'partials/single_page.html', {
        'homepage': homepage,
        'site_settings': site_settings,
        'about': about,
        'testimonials': testimonials,
        'show_testimonial_loop': show_testimonial_loop,
        'contact_form': contact_form,
        'portfolios': portfolios,
        'team_members': team_members,
    })


# class HomepageView(TemplateView):
#     template_name = "pages/home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['homepage'] = Homepage.objects.first()  # assuming only one instance
#         return context
