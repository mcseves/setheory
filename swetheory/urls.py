from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # redireciona pagina inicial
    # path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    url(r'^$', views.home, name='home'),
    path('area/<int:pk>', views.area, name='area'),

]