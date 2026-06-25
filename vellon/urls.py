from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('stores/', include('stores.urls')),
    path('api/stores/', include('stores.urls')),

    path('products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
    path('orders/', include('orders.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('notifications/', include('notifications.urls')),
    path('api/messaging/', include('messaging.urls')),
    path('messages/', include('messaging.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
