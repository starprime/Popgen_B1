from django.conf.urls import url
from . import views

urlpatterns = [
    #/EnterPage/
    url(r'^$',views.index,name='index'),

    #EnterPage/13/
    url(r'^(?P<job_id>[0-9]+)/$',views.job_details,name='job_details'),

    #
]
