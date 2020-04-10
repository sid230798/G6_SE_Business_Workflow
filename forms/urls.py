from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.index, name='index'),
    path('createform', views.createform, name='createform'),
    path('parseFormTemplate', views.parseFormTemplate, name='parseFormTemplate'),
    url(r'^validate_title/$' , views.validate_title, name='validate_title')

]