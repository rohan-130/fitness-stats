from django.shortcuts import render, redirect
from .models import User

def addExerciseView(request):
	return render(request, "addExercise.html")

def makePlanView(request):
	return render(request, "makePlan.html")

#users = User.objects.all() # to fetch all the data from the database