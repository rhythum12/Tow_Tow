from django.contrib import admin
from django.urls import path,include

from .views import *


urlpatterns = [
    path('',index,name="getAll"),
    path('get_user_billbook/<str:user_id>/<str:category>/',getUserBillBook,name="get-user-billbook"),
    path('post/',postBillBook,name="post"),
    path("update/<str:uid>/",updateBillBook,name="update"),
    path("get/<str:uid>/",getBillbook,name="getById"),
    path("delete/<str:uid>/",deleteBillBook,name="delete")
]