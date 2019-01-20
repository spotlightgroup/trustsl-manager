# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Merchant, Terminal, Transaction, ARQC, Card


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ['terminal_id', 'merchant_email', 'base',
                    'tips', 'batch_no', 'trace_no', 'date']

    def merchant_email(self, obj):
        return obj.merchant.email

    def terminal_id(self, obj):
        return obj.terminal.id


class ARQCAdmin(admin.ModelAdmin):
    model = ARQC
    list_display = ['ATC', 'TSI', 'TVR', 'AID', 'app_label']


class CardAdmin(admin.ModelAdmin):
    model = Card
    list_display = ['no', 'exp_date']


class TerminalAdmin(admin.ModelAdmin):
    model = Terminal
    list_display = ['id']


class MerchantAdmin(admin.ModelAdmin):
    model = Merchant
    list_display = ['id', 'email', 'phone']


admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Terminal, TerminalAdmin)
admin.site.register(ARQC, ARQCAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Transaction, TransactionAdmin)
