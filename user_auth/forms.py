from django import forms
from . import models
from django.contrib.auth import forms as auth_forms

#ログインフォーム
class LoginForm(auth_forms.AuthenticationForm):
    class Meta:
        model = models.CustomUser
        fields = (
            "username", "password"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'ユーザ名'

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'パスワード'

#ユーザ登録フォーム
class RegisterForm(auth_forms.UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = (
            "username","password1", "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'ユーザ名'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'パスワード（確認）'

#パスワード変更
class PasswordChangeForm(auth_forms.PasswordChangeForm):
    class Meta:
        model = models.CustomUser
        field_order = (
            'old_password', 'new_password1', 'new_password2',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #
        # self.field_order['old_password'].widget.attrs['class'] = 'form-control'
        # self.field_order['old_password'].widget.attrs['placeholder'] = '現在のパスワード'
        #
        # self.field_order['new_password1'].widget.attrs['class'] = 'form-control'
        # self.field_order['new_password1'].widget.attrs['placeholder'] = '新パスワード'
        #
        # self.field_order['new_password2'].widget.attrs['class'] = 'form-control'
        # self.field_order['new_password2'].widget.attrs['placeholder'] = '新パスワード（確認）'

# #パスワードリセット
# class PasswordResetForm(auth_forms.PasswordResetForm):
#     # email = forms.EmailField(label=("Email"), max_length=254,attrs={'class': 'form-control'})
#     email = forms.EmailField(label=("Email"), max_length=254)
