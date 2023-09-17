from django.urls import path

from . import views

urlpatterns = [
    path('', views.receiversservereception_view, name='receiversservereception'),
]
