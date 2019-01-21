from . import views
from django.conf.urls import url, include
from django.urls import path
from api.viewSets import router
from api import views


urlpatterns = [
    path('sendmail/', views.mailer, name='mailer'),
    path('receipt/<int:id>/', views.receipt, name='home'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
