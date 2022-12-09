from django.urls import path
from test1 import views

urlpatterns = [
    path('Home/', views.fun2),
    path('login/', views.empperforview),
]