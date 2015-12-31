# -*- coding: UTF-8 -*-

from rest_framework import serializers
from rest_framework import viewsets

from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact


class ContactViewSet(viewsets.ModelViewSet):
    """
    Vista que gestiona la API de contactos de cada cliente
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
