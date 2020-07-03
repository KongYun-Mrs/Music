#   !/usr/bin/env python3
#   -*- coding: utf-8 -*-
#   Created on 2019-08-08  16:00


from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env

