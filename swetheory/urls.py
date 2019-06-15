from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # redireciona pagina inicial
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('areas$', views.area)
]