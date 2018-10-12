from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.IndexView.as_view(),name="index"),
    path('mypage/', views.MyPageView.as_view(),name="mypage"),
    path('register/', views.RegisterView.as_view(),name="register"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    #パスワードリセット関連
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset_done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # path('updateprofile/', views.UpDateProfile.as_view(), name='updateprofile')
    path('updateprofile/<int:pk>/', views.UpDateProfile.as_view(), name='updateprofile')
    # path('^updateprofile/(?P<pk>[\w-]+)$', views.UpDateProfile.as_view(), name='updateprofile')
]
