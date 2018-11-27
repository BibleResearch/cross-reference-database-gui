#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from api import views

app_name = 'api'
urlpatterns = [
    url(r'^users/$', views.UserView.as_view())
]
