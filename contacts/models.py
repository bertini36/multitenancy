# -*- coding: UTF-8 -*-

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=64)
    surnames = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'