from django.urls import path

from . import views

urlpatterns = [
    path('', views.attackersfaults_views, name='attackersfaults'),
]
