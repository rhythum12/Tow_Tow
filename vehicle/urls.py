from django.contrib import admin
from django.urls import path,include

from .views import *


urlpatterns = [
    path('',index,name="getAll"),
    path('users/<str:id>/',getVehicleForUser,name="user_vehicle"),
    path('post/',postVehicle,name="post"),
    path("update/<str:uid>/",updateVehicle,name="update"),
    path("get/<str:uid>/",getVehicleById,name="getById"),
    path("delete/<str:uid>/",deleteVehicle,name="delete")
]