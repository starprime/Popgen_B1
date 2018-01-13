# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.core.urlresolvers import reverse


# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('EnterPage:user_details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.username

class Job(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    job_priority=models.CharField(max_length=5)
    job_name=models.CharField(max_length=50)
    is_fav=models.BooleanField(default=False)
    file=models.FileField(blank=True,null=True)

    def __str__(self):
        return self.job_name

        ##pronblem here
        ##python manage.py makemigrations EnterPage

#  Django Tutorial for Beginners - 17 - Adding Songs to our Database
