from rest_framework import routers, viewsets
from api.models import Card
from api.serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


router = routers.DefaultRouter()

router.register('cards', CardViewSet)
