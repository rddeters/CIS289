from django.urls import path

from . import views

urlpatterns = [
    path('', views.diggersfaults_view, name='diggersfaults'),
]
