
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tsevent/', include('tsevent.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""if settings.DEBAG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""