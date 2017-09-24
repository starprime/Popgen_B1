from django.conf.urls import url
from . import views

app_name='EnterPage'
## loof for cross site request forgery
urlpatterns = [
    #/EnterPage/
    url(r'^$',views.index,name='index'),

    #EnterPage/13/
    #EnterPage/job_id
    url(r'^(?P<user_id>[0-9]+)/$',views.user_details,name='user_details'),

    #EnterPage/<album_id>/favorite
    url(r'^(?P<user_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),

]
