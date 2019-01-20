from . import views
from django.conf.urls import url, include

from api.viewSets import router
from api import views


urlpatterns = [
    url(r'^receipt/(?P<id>\w{1,50})/$', views.index, name='home'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
