
from django.urls import path

# from app.views import create_movie

from .views import *
from . import views

urlpatterns = [
 
    path('', views.listt, name='listt.html'),
    

]


