from django.urls import path

from . import views

urlpatterns = [
    path('', views.settersrunningsets_view, name='settersrunningsets'),
]
