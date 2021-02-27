from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home')
]