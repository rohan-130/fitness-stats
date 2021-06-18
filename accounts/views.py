from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']

		if User.objects.filter(username=username).exists():
			messages.info(request, "Username Taken!")
			return redirect('register')
		elif User.objects.filter(email=email).exists():
			messages.info(request, "An account with this email already exists!")
			return redirect('register')
		elif first_name == "" or username == "" or email == "" or password == "":
			messages.info(request, "Please enter all details!")
			return redirect('register')
		else:
			user = User.objects.create_user(first_name=first_name, email=email, username=username, password=password)
			user.save()
			auth.login(request, user)
			return redirect('/fitness/plan')

	else:	
		return render(request, 'register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		if username == "" or password == "":
			messages.info(request, "Please enter all details!")
			return redirect('login')
		else:
			user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/fitness/plan')
		else:
			messages.info(request, "Incorrect Credentials!")
	return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def redirectPage(request):
	if request.user.is_authenticated:
		return redirect('/fitness/plan')
	return redirect('login')
