from django.conf.urls import url
from django.contrib import admin

from mm import views

urlpatterns = [
    
    url(r'^$', views.index, name='blog_index'),
    
]
