from django.shortcuts import render, redirect
from track.models import Exercises, Day
from django.contrib import messages
from datetime import datetime, date
from django.db.models import Q

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
				exercise = Exercises(exercise_name=exercise_name, exercise_time=exercise_time, creator_id=user_id, mon=mon, tue=tue, wed=wed, thu=thu, fri=fri, sat=sat, sun=sun)
				exercise.save()
			else:
				exercise_id = request.POST['submit']
				Exercises.objects.all().filter(id=exercise_id).delete()
		plan_list = Exercises.objects.filter(creator_id=user_id)
		return render(request, "makePlan.html", {"plan_list": plan_list})
	else:
		return redirect("/accounts/login")

def tasksView(request):
	user_id = request.user.id
	if user_id is not None:
		if request.method == 'POST':
			exercise_id = request.POST.get('doneExercise', None)
			day_object = Day(user_id=user_id, today = date.today(), exercise_id=exercise_id)
			day_object.save()
		exercise_done_qs = Day.objects.filter(user_id=user_id, today=date.today())
		exercise_done_list = [a.exercise_id for a in exercise_done_qs]
		mon =  tue = wed = thu = fri = sat = sun = 0
		day = datetime.now().weekday()
		day_name = "none"
		if day == 0:
			exercise_list = Exercises.objects.filter(creator_id=user_id, mon=1).exclude(id__in=exercise_done_list)
			day_name = "Monday"
		if day == 1:
			exercise_list = Exercises.objects.filter(creator_id=user_id, tue=1).exclude(id__in=exercise_done_list)
			day_name = "Tuesday"
		if day == 2:
			exercise_list = Exercises.objects.filter(creator_id=user_id, wed=1).exclude(id__in=exercise_done_list)
			day_name = "Wednesday"
		if day == 3:
			exercise_list = Exercises.objects.filter(creator_id=user_id, thu=1).exclude(id__in=exercise_done_list)
			day_name = "Thursday"
		if day == 4:
			exercise_list = Exercises.objects.filter(creator_id=user_id, fri=1).exclude(id__in=exercise_done_list)
			day_name = "Friday"
		if day == 5:
			exercise_list = Exercises.objects.filter(creator_id=user_id, sat=1).exclude(id__in=exercise_done_list)
			day_name = "Saturday"
		if day == 6:
			exercise_list = Exercises.objects.filter(creator_id=user_id, sun=1).exclude(id__in=exercise_done_list)
			day_name = "Sunday"

		Day.objects.filter(~Q(today = date.today())).delete()
		return render(request, "tasks.html", {"exercise_list": exercise_list, "day": day_name})
	else:
		return redirect("/accounts/login")

def logView(request):
	return render(request, 'log.html')