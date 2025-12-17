from django.urls import path
from myapp.views import *
urlpatterns = [
    path("",index,name="index"),
    path("login",user_login,name="user_login"),
    path("logout",user_logout,name="logout")
]