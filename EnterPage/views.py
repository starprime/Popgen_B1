# -*- coding: utf-8 -*-

from django.http import Http404
from .models import Job,User
from django.shortcuts import render
#from django.template import loader

from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse

## should have minimal HTML code inside Python

def index(request):
    all_user=User.objects.all()
    #template=loader.get_template('EnterPage/index.html')
    print all_user
    context = {'all_user':all_user}

    '''html=''
    for job in all_jobs:
        url='/enterpage/'+str(job.id)+'/'
        html+='<a href="'+url+'">'+job.job_name+'</a><br>'
    return HttpResponse(html)
    '''
    #return HttpResponse(template.render(context,request))
    return render(request,'EnterPage/index.html',context)


def user_details(request,user_id):
    '''try:
        user=User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exsist")
    '''
    user=get_object_or_404(User,pk=user_id)
    return render(request,'EnterPage/Detail.html',{'user':user})

def favorite(request,user_id):
    user=get_object_or_404(User,pk=user_id)
    try:
        fav_job=user.job_set.get(pk=request.POST['job'])
        print fav_job
    except(KeyError,Job.DoesNotExist):
        return render(request, 'EnterPage/Detail.html', {
            'user': user,
            'error_message':"Not a valid Job",
        })
    else:
        print fav_job,'is true'
        fav_job.is_fav = True
        fav_job.save()
        return render(request, 'EnterPage/Detail.html', {'user': user})