from django.conf.urls import url

from mm import views

urlpatterns = [
    
    url(r'^$', views.index, name='im_index'),
#     url(r'^$', views.index),

    url(r'^index/$', views.index, name='mm_index'),
    
    url(r'^mm_actions/$', views.mm_actions, name='mm_actions'),

    url(r'^time/$', views.today_is, name='todays_time'),
    
]
