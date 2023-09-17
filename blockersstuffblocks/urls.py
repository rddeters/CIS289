from django.urls import path

from . import views

urlpatterns = [
    path('', views.blockersstuffblocks_view, name='blockersstuffblocks'),
]
