from django.db import models

class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('ui', 'UI/UX Design'),
        ('development', 'Development'),
        ('photography', 'Photography'),
        ('marketing', 'Marketing'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()
    detail_url = models.URLField(default="#") 

    def category_css_class(self):
        return f'filter-{self.category}'
    
    def category_label(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, '')
    
    def __str__(self):
        return self.title
