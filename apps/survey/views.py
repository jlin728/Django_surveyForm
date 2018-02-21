# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    counter = request.session.get('counter', 0)
    request.session['counter'] = counter + 1


    return render (request, 'survey/index.html')


def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect ('/result')


def result(request):

    return render (request, 'survey/result.html')