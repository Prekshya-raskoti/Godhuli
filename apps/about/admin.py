# home/admin.py

from django.contrib import admin
from .models import AboutSection , FeatureItem, Testimonial

admin.site.register(AboutSection)

admin.site.register(FeatureItem)

admin.site.register(Testimonial)