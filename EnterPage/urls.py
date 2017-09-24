from django.conf.urls import url
from . import views

app_name='EnterPage'

urlpatterns = [
    #/EnterPage/
    url(r'^$',views.index,name='index'),

    #EnterPage/13/
    #EnterPage/job_id
    url(r'^(?P<user_id>[0-9]+)/$',views.user_details,name='user_details'),

    #
]
