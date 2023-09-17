"""
Program: home\views.py
Author: River Deters
Last date modified: 07/28/2023

"""

# Create your views here.

from django.shortcuts import render

def home_view(request):
    return render(request, 'home/index.html')
