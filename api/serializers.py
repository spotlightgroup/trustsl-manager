from rest_framework import serializers

from api.models import Card, Terminal, Marchant, Transaction, ARQC


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('no', 'exp_date')
