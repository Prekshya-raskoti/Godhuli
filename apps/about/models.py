from django.db import models

class AboutSection(models.Model):
    heading = models.CharField(max_length=255, default="About")
    sub_heading = models.CharField(max_length=255, default="Learn More About Us")
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    years_of_expertise = models.CharField(max_length=50, default="20+")
    expertise_text = models.CharField(max_length=100, default="Years of Expertise")

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.title

class FeatureItem(models.Model):
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='features')
    icon = models.CharField(max_length=50, help_text="Bootstrap Icon class (e.g. bi-check-circle-fill)")
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonials/')
    rating = models.FloatField(default=5.0, help_text="Rating out of 5 (can use 4.5, 5, etc.)")
    quote = models.TextField()

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} - {self.position}"
