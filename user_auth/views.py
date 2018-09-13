from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.contrib.auth import views as auth_views
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as auth_user

class IndexView(generic.TemplateView):
    template_name = 'index.html'

#ログイン
class LoginView(auth_views.LoginView):
    template_name='login.html'
    authentication_form=forms.LoginForm

#ログアウト
class LogoutView(auth_views.LogoutView):
    template_name='index.html'

#ユーザ登録
class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('user_auth:index')

#ユーザ情報更新
class UpDateProfile(generic.UpdateView):
    model = auth_user
    form_class = forms.RegisterForm
    template_name = 'updateprofile.html'
    success_url = reverse_lazy('user_auth:mypage')

#「LoginRequiredMixin」でログイン時のみ表示
class MyPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mypage.html'
