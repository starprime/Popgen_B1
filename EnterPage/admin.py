# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import User,Job

admin.site.register(User)
admin.site.register(Job)

