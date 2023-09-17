from django.urls import path

from . import views

urlpatterns = [
    path('', views.serversaces_view, name='serversaces'),
]
