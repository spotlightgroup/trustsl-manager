# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Marchant, Terminal, Transaction, ARQC, Card

admin.site.register(Marchant)
admin.site.register(Terminal)
admin.site.register(Transaction)
admin.site.register(ARQC)
admin.site.register(Card)
