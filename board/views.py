# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from .models import Photo , Entries
from django.template import Context, loader
from django import forms

def read(request, entry_id=None):
    page_title = '블로그 글 읽기 화면'

    current_entry = Entries.objects.get(id=int(entry_id))

    return HttpResponse('안녕, 여러분. [%d]번 글은 [%s]이야.' % (current_entry.id, current_entry.Title.encode('utf-8')))


def test(request):

    class NameForm(forms.Form):

        test = forms.CharField(label = 'Your name', max_length = 100)

    t = loader.get_template('test.html')
    c = Context({
            'foo':'bar'
        })

    if request.method =='POST':

        form = NameForm(request.POST)

        if form.is_valid():

            value = form.cleaned_data['test']

            return HttpResponse('감사합니다. %s' % (value.encode('utf-8')))
    else:
            form = NameForm()

    return render(request, 'main.html', {'form' : form})    