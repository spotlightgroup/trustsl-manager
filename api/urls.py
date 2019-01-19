from . import views
from django.conf.urls import url, include

from api.viewSets import router

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
