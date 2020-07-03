#   !/usr/bin/env python3
#   -*- coding: utf-8 -*-
#   Created on 2019-08-08  15:31
from django.conf.urls import url

from Admin import views

urlpatterns = [
    url('^test/$', views.test)
]

