from django.shortcuts import render, redirect
from track.models import Exercises, Day, Month
from django.contrib import messages
from datetime import datetime, date
from django.db.models import Q
from json import dumps

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
		return render(request, "makePlan.html", {"plan_list": plan_list, "length": len(plan_list)})
	else:
		return redirect("/accounts/login")

def tasksView(request):
	user_id = request.user.id
	if user_id is not None:
		mon =  tue = wed = thu = fri = sat = sun = 0
		day = datetime.now().weekday()
		day_name = "none"
		if day == 0:
			exercise_list = Exercises.objects.filter(creator_id=user_id, mon=1)
			day_name = "Monday"
		if day == 1:
			exercise_list = Exercises.objects.filter(creator_id=user_id, tue=1)
			day_name = "Tuesday"
		if day == 2:
			exercise_list = Exercises.objects.filter(creator_id=user_id, wed=1)
			day_name = "Wednesday"
		if day == 3:
			exercise_list = Exercises.objects.filter(creator_id=user_id, thu=1)
			day_name = "Thursday"
		if day == 4:
			exercise_list = Exercises.objects.filter(creator_id=user_id, fri=1)
			day_name = "Friday"
		if day == 5:
			exercise_list = Exercises.objects.filter(creator_id=user_id, sat=1)
			day_name = "Saturday"
		if day == 6:
			exercise_list = Exercises.objects.filter(creator_id=user_id, sun=1)
			day_name = "Sunday"


		if request.method == 'POST':
			exercise_id = request.POST.get('doneExercise', None)
			day_object = Day(user_id=user_id, today = date.today(), exercise_id=exercise_id)
			day_object.save()
			if len(Day.objects.filter(user_id=user_id, today = date.today(), exercise_id=exercise_id)) == 1:
				month_filter = Month.objects.filter(user_id=user_id, date=date.today())
				if len(month_filter) == 0:
					month_object = Month(user_id=user_id, date=date.today(), number_done=1, total_number=len(exercise_list))
					month_object.save()
				else:
					m_id = Month.objects.get(user_id=user_id, date=date.today()).id
					m_done = Month.objects.get(user_id=user_id, date=date.today()).number_done
					m_object = Month(id=m_id, user_id=user_id, date=date.today(), number_done=(m_done+1), total_number=len(exercise_list))
					m_object.save()
				
		exercise_done_qs = Day.objects.filter(user_id=user_id, today=date.today())
		exercise_done_list = [a.exercise_id for a in exercise_done_qs]

		exercise_list = exercise_list.exclude(id__in=exercise_done_list)

		Day.objects.filter(~Q(today = date.today())).delete()
		return render(request, "tasks.html", {"exercise_list": exercise_list, "day": day_name})
	else:
		return redirect("/accounts/login")

def logView(request):
	user_id = request.user.id
	list_dates = []
	list_score = []
	for day in Month.objects.filter(user_id=user_id):
		list_dates.append(str(day.date))
		score = (day.number_done/day.total_number)*100
		list_score.append(score)

	data = dumps({"list_dates": list_dates, "list_score": list_score})

	return render(request, 'log.html', {"data": data})

def blog(request):
	return render(request, 'blog.html')