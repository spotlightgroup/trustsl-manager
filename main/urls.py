from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api/', include('api.urls')),
    url(r'^$', serve,kwargs={'path': 'index.html'}),   
    url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
    RedirectView.as_view(url='/static/%(path)s', permanent=False)), 
]
