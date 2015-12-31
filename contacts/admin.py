# -*- coding: UTF-8 -*-

from django.contrib import admin
from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'surnames', 'email', 'phone_number')
    search_fields = ['name', 'surnames', 'email', 'phone_number']
    list_filter = ('name', 'surnames', 'email', 'phone_number')

admin.site.register(Contact, ContactAdmin)
