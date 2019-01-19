from rest_framework import serializers

from api.models import Card, Terminal, Marchant, Transaction, ARQC


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('no', 'exp_date')


class TerminalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Terminal
        fields = ('id', )


class MarchantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marchant
        fields = ('id', 'email', 'phone')


class ARQCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ARQC
        fields = ('ATC', 'TSI', 'TVR', 'AID', 'app_label')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'type', 'batch_no', 'trace_no', 'exp_date',
            'ref_no', 'app_code', 'base',
            'tips', 'signature_img', 'arqc',
            'card', 'terminal', 'marchant'
        )
