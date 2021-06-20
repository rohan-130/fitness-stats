from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add', views.addExerciseView, name="add"),
    path('plan', views.makePlanView, name="plan"),
    path('tasks', views.tasksView, name="tasks"),
    path('health', views.health, name="health"),
]
