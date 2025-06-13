from django.shortcuts import render
from apps.about.models import AboutSection, Testimonial

def about_view(request):
    about = AboutSection.objects.prefetch_related('features').first()
    testimonials = Testimonial.objects.all()
    show_testimonial_loop = testimonials.count() > 2

    return render(request, 'partials/about.html', {
        'about': about,
        'testimonials': testimonials,
        'show_testimonial_loop': show_testimonial_loop,
    })
