
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages


class UserManager(models.Manager):
	def validate_user(request, postData):
		errors = {}

		#Validate name
		if len(postData['first_name']) < 3:
			errors['first_name'] = "First name must be longer than 3 characters"

		if len(postData['last_name']) < 3:
			errors['last_name'] = "Last name must be longer than 3 characters"

		#Validate email
		if len(postData['email']) < 4:
			errors['email'] = "Email must be longer than 4 characters"

		#Validate password

		if len(postData['password']) < 8:
			errors['password'] = "Password must be longer than 8 characters"

			if postData['password'] != postData['cnfrm_password']:
					errors['cnfrm_password'] = "Passwords do not match"

		return errors

class QuoteManager(models.Manager):
	def validate_quote(request, postData):
		errors = {}

		if len(postData['quote']) > 100:
			errors['quote'] = "100 characters or less"

		if len(postData['quote']) == 0:
			errors['quote'] = "Field cannot be blank"

		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Quote(models.Model):
	quote = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, related_name="quotes")
	objects = QuoteManager()




