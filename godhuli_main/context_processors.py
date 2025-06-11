from apps.home.models import SiteSetting

def site_settings(request):
    site_setting = SiteSetting.objects.first() 
    return {
        'site_setting': site_setting
    }
