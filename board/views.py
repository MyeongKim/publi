# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, loader
from django import forms
from django.forms import ModelForm
from django.views import generic
from . import models
#example copy start ========


class Timeline(generic.ListView):

    _shared_state = {}
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2
    def __new__(cls, *args, **kwargs):
        obj = super(Timeline, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class Post(generic.DetailView):

    model = models.Entry
    template_name = "post.html"

def createPost(request):

    form = models.EntryForm()

    if request.method == 'POST':
        form = models.EntryForm(request.POST)

        if form.is_valid():

            entry = form.save()

            return redirect('/')

    return render(request, 'write.html', {'form' : form})
