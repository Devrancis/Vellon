import zoneinfo
from django.utils import timezone

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Default to Africa/Lagos as per settings
        tzname = "Africa/Lagos"
        
        # In the future, this could be based on request.user.timezone
        # if request.user.is_authenticated and hasattr(request.user, 'timezone'):
        #     tzname = request.user.timezone
            
        timezone.activate(zoneinfo.ZoneInfo(tzname))
        return self.get_response(request)
