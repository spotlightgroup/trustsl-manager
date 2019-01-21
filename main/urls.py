from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api/', include('api.urls')),
    url(r'^$', serve, kwargs={'path': 'index.html'}),
    url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
