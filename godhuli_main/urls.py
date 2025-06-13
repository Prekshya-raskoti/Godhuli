from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.home.views import single_page_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', single_page_view, name='home'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
