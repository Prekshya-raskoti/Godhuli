# home/models.py

from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='site/logo/', blank=True, null=True)
    tagline = models.CharField(max_length=255, blank=True)
    about_company = models.TextField(blank=True)
    company_name = models.CharField(max_length=255, default="Godhuli IT Solutions Pvt. Ltd.")

    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    get_started_text = models.CharField(max_length=50, default="Get Started")
    get_started_url = models.URLField(blank=True, null=True)
    footer_notice = models.CharField(max_length=255, default="All Rights Reserved")

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name


class SocialLink(models.Model):
    site = models.ForeignKey(SiteSetting, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=100)  # bi bi-twitter, etc.
    url = models.URLField()

    def __str__(self):
        return self.platform

class Homepage(models.Model):
    agency_title = models.CharField(max_length=100, default="OUR AGENCY")
    main_heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    cta_text = models.CharField(max_length=50, default="EXPLORE SERVICES")
    cta_link = models.URLField(max_length=500)
    stats_number = models.CharField(max_length=20, default="5K")
    stats_label = models.CharField(max_length=100, default="Successful Campaigns")
    stats_link = models.URLField(max_length=500, blank=True, null=True)
    hero_image = models.ImageField(upload_to='homepage/', blank=True, null=True)

    class Meta:
        verbose_name = "Homepage Content"
        verbose_name_plural = "Homepage Content"

    def __str__(self):
        return "Homepage Content"
