# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
import json

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2048, default='(нет описания)')
    def_path = settings.MEDIA_ROOT+'thumbnails/default.jpg'
    thumbnail = models.ImageField(upload_to='thumbnails/', default=def_path)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class BasketedProduct(models.Model):
    product = models.ManyToManyField(Product)
    session = models.CharField(max_length=128)

    #def __str__(self):
    #    return 'qwerty123' #json.dumps()
