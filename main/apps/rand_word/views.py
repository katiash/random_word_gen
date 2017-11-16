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
    try:
        request.session['tries']
    except KeyError:
        request.session['tries']=0

    return render(request,'rand_word/index.html', context)

# IF WE RETURN JUST THE RAW TEMPLATE FILE, THE 'context' dictionary in the "index" method
# is not defined.
# IF WE RETURN REDIRECT to the ROUTE (root route) that calls 'Index' method,
# the 'context' dictionary again gets generated and we see result on the page.
 
def generate(request):
    request.session['tries'] += 1
    request.session['word']= get_random_string(14)
    # return render(request, 'rand_word/index.html')
    return redirect('/')

def reset(request):
    del request.session['tries']
    del request.session['word']
    return redirect('/')

# Example: get_random_string(length=14) gets a random string
# of legth 14. 