
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from .models import *
from django.contrib import messages


def index(request):
	return render(request, "blog/index.html")

def register(request):
	errors = User.objects.validate_user(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/')

	else:
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

		User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed_pw)

		user = User.objects.get(first_name=first_name)
		request.session['id'] = user.id
		return redirect('/')

def login(request):
	#sets post data equal to variables. Then filters the email to see if it is equal to one saved in the database previously with the register form. 
	#Checks to see if there was an email entered, if there was checks to see if password entered matches one entered into the database. 
	email = request.POST['email']
	password = request.POST['password']

	user = User.objects.filter(email=email)

	if len(user) > 0:
		this_password = bcrypt.checkpw(password.encode(), user[0].password.encode())
		if this_password:
			request.session['id'] = user[0].id
			return redirect('/dashboard')
		else:
			messages.error(request, "Incorrect username/password combination.")
			return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')

def dashboard(request):
	context = {
		"user": User.objects.get(id=request.session['id']),
		"quotes": Quote.objects.all()
	}
	return render(request, "blog/dashboard.html", context)

def comment(request):
	errors = Quote.objects.validate_quote(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/dashboard')

	else:
		quote = request.POST['quote']
		user = User.objects.get(id=request.session['id'])
		comment = Quote(quote=quote, added_by=user.first_name)
		comment.save()
		comment.user.add(user)
		return redirect("/dashboard")

def user_profile(request, id):
	user = User.objects.get(id=id)
	context = {
		"user": User.objects.get(id=id),
		"quotes": Quote.objects.filter(added_by=user.first_name)
	}
	return render(request, "blog/profile.html", context)



