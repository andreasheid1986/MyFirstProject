from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('more/', views.more, name='more'),
    path('error_message_app/', views.error_message_app, name='error_message_app'),
]