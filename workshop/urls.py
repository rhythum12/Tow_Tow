
from django.urls import path

from .views import *


urlpatterns = [
    path("",WorkshopApi.as_view()),
    path("get/<int:pk>/",WorkshopDetailApi.as_view()),
    path("post/",WorkshopCreateApi.as_view()),
    path("update/<int:pk>/",WorkshopUpdateApi.as_view()),
    path("delete/<int:pk>/",WorkshopDeleteApi.as_view()),    
]
