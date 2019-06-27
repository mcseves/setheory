from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # redireciona pagina inicial
    # path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    url(r'^$', views.home, name='home'),
    path('area/<str:name>', views.area_of_interest, name='area_of_interest'),
    path('area/<str:name>/new/', views.new_theory, name='new_theory'),
    path('search_theory/', views.search_theory, name='search_theory'),
    path('area/<str:name>/new/addconstruct/', views.add_construct, name='add_construct'),
    path('area/<str:name>/new/addvalue/', views.add_value, name='add_value')
]
