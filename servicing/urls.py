from django.contrib import admin
from django.urls import path,include

from .views import *


urlpatterns = [
    path('',index,name="getAll"),
    path("get_user_servicing/<str:user_id>/<str:category>/",getUserServicing,name="getById"),
    path('post/',postServicing,name="post"),
    path("update/<str:uid>/",updateServicing,name="update"),
    path("get/<str:uid>/",getServicing,name="getById"),
    path("delete/<str:uid>/",deleteServicing,name="delete")
]