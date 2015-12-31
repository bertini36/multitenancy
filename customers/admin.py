# -*- coding: UTF-8 -*-

from django.contrib import admin
from customers.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'paid_until', 'on_trial', 'created_on')
    search_fields = ['name', 'paid_until', 'on_trial', 'created_on']
    list_filter = ('name', 'paid_until', 'on_trial', 'created_on')

admin.site.register(Client, ClientAdmin)
