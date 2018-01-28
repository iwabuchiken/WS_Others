from django.conf.urls import url

from im import views

urlpatterns = [
    
    url(r'^$', views.index, name='im_index'),
#     url(r'^$', views.index),

]
