from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.About.as_view(), name='about')
]