from rest_framework import serializers

from api.models import Card, Terminal, Merchant, Transaction, ARQC


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('no', 'exp_date')


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = ('id', )


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ('id', 'email', 'phone')


class ARQCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARQC
        fields = ('ATC', 'TSI', 'TVR', 'AID', 'app_label')


class TransactionSerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer()
    terminal = TerminalSerializer()
    arqc = ARQCSerializer()
    card = CardSerializer()

    class Meta:
        model = Transaction
        fields = (
            'id', 'type', 'batch_no', 'trace_no', 'date',
            'ref_no', 'app_code', 'base', 'receiptPDF',
            'tips', 'signature_img', 'merchant', 'terminal', 'arqc', 'card'
        )
