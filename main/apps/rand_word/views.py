# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Importing get_random_string from django.utils.crypto..
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    
    context={
        "mystr" : get_random_string(14)
    }
    return render(request,'rand_word/index.html', context)

# Example: get_random_string(length=14) gets a random string
# of legth 14. 