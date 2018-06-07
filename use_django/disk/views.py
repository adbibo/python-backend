from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse

from models import User


# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            headimg = uf.cleaned_data['headImg']

            user = User()
            user.username = username
            user.headImg = headimg

            user.save()

            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render_to_response('disk/register.html', {'uf': uf})
