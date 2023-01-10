from django.contrib import admin
from django.urls import path,include

from .views import *


urlpatterns = [
    path('',index,name="getAll"),
    path('post/',postUser,name="post"),
    path("update/<str:id>/",updateUser,name="update"),
    path("get/<str:uid>/",getUserById,name="getById"),
    path("delete/<str:uid>/",deleteUser,name="delete")
]