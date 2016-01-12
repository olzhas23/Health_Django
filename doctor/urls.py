from django.conf.urls import url
from django.contrib import admin
from doctor import views
#add more
urlpatterns = [
    url(r'', views.index),
    url(r'^search/', views.search),
    url(r'^cp/$', views.existing_patient,
name="create_patient")
]