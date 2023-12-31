from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homeApp.urls')),
    path('', include('Accounts.urls')),
    path('', include('shopApp.urls')),
    path('', include('adminApp.urls')),
    path('', include('orderApp.urls')),
    path('', include('paymentApp.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
