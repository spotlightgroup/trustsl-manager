# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Marchant, Terminal, Transaction, ARQC, Card


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ['terminal_id', 'marchant_email', 'base',
                    'tips', 'batch_no', 'trace_no', 'date']

    def marchant_email(self, obj):
        return obj.marchant.email

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


class MarchantAdmin(admin.ModelAdmin):
    model = Marchant
    list_display = ['id', 'email', 'phone']


admin.site.register(Marchant, MarchantAdmin)
admin.site.register(Terminal, TerminalAdmin)
admin.site.register(ARQC, ARQCAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Transaction, TransactionAdmin)
