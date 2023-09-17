from django.urls import path

from . import views

urlpatterns = [
    path('', views.serversfaults_view, name='serversfaults'),
]
