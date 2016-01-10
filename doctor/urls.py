from django.conf.urls import url
from django.contrib import admin
from doctor import views
urlpatterns = [
    url(r'$', views.Docotor_Info.as_view()),
    url(r'^list/',views.doctors),

]