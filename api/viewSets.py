from rest_framework import routers, viewsets
from api.models import Card, Terminal
from api.serializers import CardSerializer, TerminalSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer


router = routers.DefaultRouter()

router.register('cards', CardViewSet)
router.register('terminals', TerminalViewSet)
