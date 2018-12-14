from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from .content.urls import urlpatterns as content_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += content_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

