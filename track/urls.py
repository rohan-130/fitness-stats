from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('plan', views.makePlanView, name="plan"),
    path('tasks', views.tasksView, name="tasks"),
    path('log', views.logView, name="log"),
]
