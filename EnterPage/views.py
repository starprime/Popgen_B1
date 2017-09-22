# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Job
from django.template import loader

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

## should have minimal HTML code inside Python

def index(request):
    all_jobs=Job.objects.all()
    template=loader.get_template('')
    '''html=''
    for job in all_jobs:
        url='/enterpage/'+str(job.id)+'/'
        html+='<a href="'+url+'">'+job.job_name+'</a><br>'
    return HttpResponse(html)
    '''
    return HttpResponse('')

def job_details(request,job_id):
    return HttpResponse("<h1> details of the job "+str(job_id)+"<h1>")
