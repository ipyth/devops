from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms

from models import User, Host


# Create your views here.

class UserForm(forms.Form):
	username = forms.CharField(label='username', max_length=100)
	password = forms.CharField(label='password', widget=forms.PasswordInput())


def login(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			user = User.objects.filter(username__exact=username, password__exact=password)
			if user:
				# response = HttpResponseRedirect('index/')
				# response.set_cookie('username',username,3600)
				return HttpResponse('login')
			else:
				return HttpResponse('username/password wrong')
	else:
		uf = UserForm()
	return render_to_response('index.html', {'uf': uf}, context_instance=RequestContext(request))


def index(request):
	host_list = Host.objects.all()
	return render(request, 'devops/index.html', locals())

# return HttpResponse('index')
