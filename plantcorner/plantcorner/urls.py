from django.contrib import admin
from django.urls import path, include
from plantsindex.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth0login.urls')),
    path('', include('plantsindex.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
