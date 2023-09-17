from django.urls import path

from . import views

urlpatterns = [
    path('', views.receiverstotalattempts_view, name='receiverstotalattempts'),
]
