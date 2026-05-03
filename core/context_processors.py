from django.conf import settings

def global_settings(request):
    """
    Adds global settings to the context.
    """
    return {
        'SITE_NAME': 'Vellon',
        'SITE_URL': getattr(settings, 'SITE_URL', 'http://localhost:8000'),
        'DEBUG': settings.DEBUG,
    }
