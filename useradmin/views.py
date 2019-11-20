from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from crudapp import forms
# Create your views here.

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "crudapp/signup.html"
    success_url = reverse_lazy('top')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

class Login(LoginView):
    form_class = forms.LoginForm
    template_name = "crudapp/login.html"
    