from rest_framework import routers, viewsets
from api.models import Card, Terminal, Marchant, Transaction, ARQC
from api.serializers import CardSerializer, TerminalSerializer, MarchantSerializer, TransactionSerializer, ARQCSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer


class MarchantViewSet(viewsets.ModelViewSet):
    queryset = Marchant.objects.all()
    serializer_class = MarchantSerializer


class ARQCViewSet(viewsets.ModelViewSet):
    queryset = ARQC.objects.all()
    serializer_class = ARQCSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


router = routers.DefaultRouter()

router.register('cards', CardViewSet)
router.register('terminals', TerminalViewSet)
router.register('marchants', MarchantViewSet)
router.register('arqc', ARQCViewSet)
router.register('transactions', TransactionViewSet)
