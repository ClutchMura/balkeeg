from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.contrib.auth import views as auth_views
from . import forms
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as auth_user
from django.contrib.auth import forms as auth_forms

class IndexView(generic.TemplateView):
    template_name = 'index.html'

#ログイン
class LoginView(auth_views.LoginView):
    template_name='login.html'
    form_class = forms.LoginForm

#ログアウト
class LogoutView(auth_views.LogoutView):
    template_name='index.html'

#ユーザ登録
class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('user_auth:index')

#パスワード変更
class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = forms.PasswordChangeForm
    success_url = reverse_lazy('user_auth:password_change_done')
    template_name = 'password_change.html'

#パスワード変更成功
class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
     template_name = 'password_change_done.html'

#パアスワードリセット
# class PasswordResetView(auth_views.PasswordResetView):
#     form_class = forms.PasswordResetForm
#     template_name = 'password_reset.html'
#     email_template_name='password_reset_email.html'
#     success_url = reverse_lazy('user_auth:password_reset_done')

#パスワードリセット変更
# class PasswordResetDoneView(auth_views.PasswordResetDoneView):
#     template_name = 'password_reset_done.html'

#ユーザ情報更新
class UpDateProfile(generic.UpdateView):
    model = auth_user
    form_class = forms.RegisterForm
    template_name = 'updateprofile.html'
    success_url = reverse_lazy('user_auth:mypage')

#「LoginRequiredMixin」でログイン時のみ表示
class MyPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mypage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        UserContact = models.UserContact.objects.filter(username_id=self.request.user.id)
        context['Contact_list'] = UserContact.values('contact_type','contact_link')
        return context
