from django.urls import path
from . import views

app_name = 'engineer'
urlpatterns = [
    path('', views.IndexView.as_view(),name="index"),
    path('mypage/', views.MyPageView.as_view(),name="mypage"),
    path('register/', views.RegisterView.as_view(),name="register"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('updateprofile/', views.UpDateProfile.as_view(), name='updateprofile')
    path('updateprofile/<int:pk>/', views.UpDateProfile.as_view(), name='updateprofile')
    # path('^updateprofile/(?P<pk>[\w-]+)$', views.UpDateProfile.as_view(), name='updateprofile')
]
