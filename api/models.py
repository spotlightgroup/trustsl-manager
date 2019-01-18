# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    Product_name = models.CharField(max_length=200)
    Product_description = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
