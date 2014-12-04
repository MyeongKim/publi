# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, loader
from django import forms
from django.forms import ModelForm
from django.views import generic
from . import models

#example copy start ========

class BlogIndex(generic.ListView):

    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2

class BlogDetail(generic.DetailView):

    model = models.Entry
    template_name = "post.html"


#example copy end ========

def read(request, entry_id=None):
    page_title = '블로그 글 읽기 화면'

    current_entry = Entries.objects.get(id=int(entry_id))

    return HttpResponse('안녕, 여러분. [%d]번 글은 [%s]이야.' % (current_entry.id, current_entry.Title.encode('utf-8')))


def login(request):

    class NameForm(forms.Form):

        test = forms.CharField(label = 'Your name', max_length = 100)

    t = loader.get_template('main.html')
    c = Context({
            'foo':'bar'
        })

    class UsersForm(ModelForm):
        class Meta:

            model = Users
            fields = ['Email', 'Password']

    if request.method =='POST':

        form = UsersForm(request.POST)

        if form.is_valid():

            all_users = Users.objects.all()

            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']

            if (all_users.filter(Email=email)):

                id = all_users.filter(Email=email)[0].id
                return redirect(reverse('write'),id=id)
            else:
                return HttpResponse('로그인에 실패하였습니다.')

    else:
            form = UsersForm()

    return render(request, 'main.html', {'form' : form})

def write(request,id):

    email = request.GET



    return HttpResponse("dsf %s" % email.encode('utf-8'))