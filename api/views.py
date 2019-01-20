# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from api.models import Transaction
from django.template import loader


def receipt(request, id):
    transaction = Transaction.objects.get(id=id)
    template = loader.get_template('api/receipt.html')
    context = {
        'receipt_data': transaction,
    }
    return HttpResponse(template.render(context, request))
