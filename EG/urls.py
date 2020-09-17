from django.contrib import admin
from django.urls import path, include
"""from blog import views
from credits import views
from general import views"""
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('credits/', include('credits.urls')),
    path("", include('general.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)