from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display/', views.displaytheories, name='displaytheories'),
    path('display/create', views.createtheories, name='createtheories')
]