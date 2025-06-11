# home/admin.py

from django.contrib import admin
from .models import SiteSetting, SocialLink ,Homepage

admin.site.register(SiteSetting)

admin.site.register(SocialLink)

admin.site.register(Homepage)
