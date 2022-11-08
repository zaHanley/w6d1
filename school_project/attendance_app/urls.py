from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student/', views.add_student)
]