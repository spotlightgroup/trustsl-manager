# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Marchant(models.Model):
    id = models.CharField(max_length=200, primary_key=True)


class Terminal(models.Model):
    id = models.CharField(max_length=200, primary_key=True)


class Card(models.Model):
    no = models.CharField(max_length=200, primary_key=True)
    exp_date = models.DateField('Exp Date')


class ARQC(models.Model):
    ATC = models.CharField(max_length=4)
    TSI = models.CharField(max_length=4)
    TVR = models.CharField(max_length=10)
    AID = models.CharField(max_length=16)
    app_label = models.CharField(max_length=50)


class Transaction(models.Model):
    type = models.CharField(max_length=50)
    batch_no = models.CharField(max_length=6)
    trace_no = models.CharField(max_length=6)
    exp_date = models.DateTimeField('date-time')
    ref_no = models.CharField(max_length=12)
    app_code = models.CharField(max_length=6)
    base = models.FloatField()
    tips = models.FloatField()
    signature_img = models.ImageField(upload_to='signatures')
