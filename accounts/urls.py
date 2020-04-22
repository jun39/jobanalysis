from django.urls import path
from . import views

# app_name = 'accounts' 動かなかったら書くやつ
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.Top.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]