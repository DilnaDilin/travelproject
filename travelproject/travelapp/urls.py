
from django.urls import path

from . import views
from .views import demo

urlpatterns = [

    path('', views.demo, name='demo'),
]