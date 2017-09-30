from django.conf.urls import url
from . import views

app_name='EnterPage'
## loof for cross site request forgery
urlpatterns = [
    #/EnterPage/
    #url(r'^$',views.index,name='index'),
    url(r'^$',views.IndexView.as_view(),name='index'),
    #EnterPage/13/
    #EnterPage/job_id
    #url(r'^(?P<user_id>[0-9]+)/$',views.user_details,name='user_details'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailsView.as_view(),name='user_details'),

    #EnterPage/<album_id>/favorite
    #url(r'^(?P<user_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
    ## add user     /enterpage/add/2
    url(r'user/add/$',views.UserCreate.as_view(),name='user_add'),

    ## update user  /enterpage/2/
    url(r'user/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name='user_update'),

    ## delete /enterpage/2/delete
    url(r'user/add/$', views.UserDelete.as_view(), name='user_delete'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

]

## rest api can be accessed by all device

