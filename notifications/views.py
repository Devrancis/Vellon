from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification

@login_required
def notification_list_view(request):
    notifications = Notification.objects.filter(recipient=request.user)[:10]
    return render(request, 'notifications/list.html', {'notifications': notifications})

@login_required
def api_get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, is_read=False).values(
        'id', 'title', 'description', 'notification_type', 'created_at', 'link'
    )[:5]
    return JsonResponse({'notifications': list(notifications)})

@login_required
def mark_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk, recipient=request.user)
    notification.is_read = True
    notification.save()
    return JsonResponse({'status': 'success'})
