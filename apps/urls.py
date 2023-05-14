from django.urls import path

from apps.views import register_view, login_view, home

urlpatterns = [
    path('register',register_view,name='register_view'),
    path('login',login_view,name='login_view'),
    path('',home,name='home')
]