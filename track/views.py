from django.shortcuts import render, redirect
from track.models import Exercises, UserLog, Plans
from django.contrib import messages
from datetime import datetime
from django.db.models import Q

def addExerciseView(request):
	user_id = request.user.id
	if request.method == 'POST':
		exercise_name = request.POST['exerciseName']
		unit = request.POST['unit']
		if exercise_name == '' or unit == '':
			messages.info(request, 'Please enter an exercise!')
		elif request.user.is_authenticated:
			exercise = Exercises(creator_id=user_id, exercise_name=exercise_name, exercise_unit=unit)
			exercise.save()
		else:
			messages.info(request, 'Please sign in!')

	exercise_list = Exercises.objects.filter(creator_id=user_id)
	return render(request, "addExercise.html", {"list": exercise_list})

def makePlanView(request):
	user_id = request.user.id
	if user_id is not None:
		if request.method == 'POST':
			if request.POST['submit'] == "Add":
				exercise_name = request.POST['exercise_name']
				exercise_time = request.POST['time']
				mon = request.POST.get('mon', default=0)
				tue = request.POST.get('tue', default=0)
				wed = request.POST.get('wed', default=0)
				thu = request.POST.get('thu', default=0)
				fri = request.POST.get('fri', default=0)
				sat = request.POST.get('sat', default=0)
				sun = request.POST.get('sun', default=0)
				plan = Plans(exercise_name=exercise_name, exercise_time=exercise_time, creator_id=user_id, mon=mon, tue=tue, wed=wed, thu=thu, fri=fri, sat=sat, sun=sun)
				plan.save()
			else:
				exercise_id = request.POST['submit']
				Plans.objects.all().filter(id=exercise_id).delete()
		exercise_list = Exercises.objects.filter(creator_id=user_id)
		plan_list = Plans.objects.filter(creator_id=user_id)
		return render(request, "makePlan.html", {"exercise_list": exercise_list, "plan_list": plan_list})
	else:
		return redirect("/accounts/login")

def tasksView(request):
	user_id = request.user.id
	if user_id is not None:
		day = datetime.now().weekday()
		plan_list = Plans.objects.filter(creator_id=user_id)
		mon =  tue = wed = thu = fri = sat = sun = 0
		day_name = "none"
		if day == 0:
			plan_list = Plans.objects.filter(creator_id=user_id, mon=1)
			day_name = "Monday"
		if day == 1:
			plan_list = Plans.objects.filter(creator_id=user_id, tue=1)
			day_name = "Tuesday"
		if day == 2:
			plan_list = Plans.objects.filter(creator_id=user_id, wed=1)
			day_name = "Wednesday"
		if day == 3:
			plan_list = Plans.objects.filter(creator_id=user_id, thu=1)
			day_name = "Thursday"
		if day == 4:
			plan_list = Plans.objects.filter(creator_id=user_id, fri=1)
			day_name = "Friday"
		if day == 5:
			plan_list = Plans.objects.filter(creator_id=user_id, sat=1)
			day_name = "Saturday"
		if day == 6:
			plan_list = Plans.objects.filter(creator_id=user_id, sun=1)
			day_name = "Sunday"

		return render(request, "tasks.html", {"plan_list": plan_list, "day": day_name})
	else:
		return redirect("/accounts/login")

def health(request):
	return render(request, 'health.html')

	


