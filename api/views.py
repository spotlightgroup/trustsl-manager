# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from api.models import Transaction
from django.template import loader
from main.settings import BASE_DIR, EMAIL_HOST_USER
from django.core.mail import EmailMessage


def receipt(request, id):
    transaction = Transaction.objects.get(id=id)
    template = loader.get_template('api/receipt.html')
    context = {
        'receipt_data': transaction,
        'amount': transaction.base + transaction.tips,
    }
    return HttpResponse(template.render(context, request))


def mailer(request):
    email = EmailMessage(
        'Subject here', 'Here is the message.', EMAIL_HOST_USER, ['z3by.ahmad@gmail.com'])
    email.attach_file(
        'media/PDFs/c41fab0fb8e1197fccd5304cb0dfcecc7a7d7ddf91aa09c92693b5e9.pdf')
    email.send()
    return HttpResponse('done')
