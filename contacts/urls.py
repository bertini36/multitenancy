# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter

from contacts.views import ContactViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )
