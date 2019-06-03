from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
from .all_choices import COLLEGE_SELECTED
from .give_default import give_to_model
from multiselectfield import MultiSelectField
from . validation import validate_zero
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class FillProfile(models.Model):
	adv_air=models.PositiveIntegerField()
	mains_air=models.PositiveIntegerField()

#Assume you have an Author model that is a ForeignKey in a Book model. Now, if you delete an instance of the Author model, 
#Django would not know what to do with instances of the Book model that depend on that instance of Author model.
#The on_delete method tells Django what to do in that case. Setting on_delete=models.CASCADE will instruct Django 
#to cascade the deleting effect i.e. delete all the Book model instances that depend on the Author model instance you
#deleted.
	Logged_in_user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	state_choices=(
				('andhra pradesh','Andhra Pradesh'),
				('arrunachal pradesh','Arrunachal Pradesh'),
				('assam','Assam'),
				('bihar','Bihar'),
				('chattisgarh','Chattisgarh'),
				('goa','Goa'),
				('gujrat','Gujrat'),
				('haryana','Haryana'),
				('himachal pradesh','Himachal Pradesh'),
				('jammu & kashmir','Jammu & Kashmir'),
				('jharkhand','Jharkhand'),
				('karnataka','Karnataka'),
				('kerala','Kerala'),
				('madhya pradesh','Madhya Pradesh'),
				('maharashtra','Maharashtra'),
				('manipur','Manipur'),
				('meghalaya','Meghalaya'),
				('mizoram','Mizoram'),
				('nagaland','Nagaland'),
				('odisha','Odisha'),
				('rajasthan','Rajasthan'),
				('sikkim','Sikkim'),
				('tamil nadu','Tamil Nadu'),
				('telangana','Telangana'),
				('tripura','Tripura'),
				('uttarakhand','Uttharakhand'),
				('uttar pradesh','Uttar Pradesh'),
				('west bengal','West Bengal'),

				)
	state=models.CharField(max_length=100,choices=state_choices)
	category_choices=(
					('general','General'),
					('obc','OBC'),
					('sc','SC'),
					('st','ST'),
					)
	category=models.CharField(max_length=100,choices=category_choices)
	
	Gender_choices=(
					(True,'Male'),
					(False,'Female'),
					)
	gender=models.BooleanField(choices=Gender_choices,default=True)

	def __str__(self):
		return str(self.Logged_in_user)

Def=give_to_model()

class FillPrefer(models.Model):
	college_selected=MultiSelectField(choices=COLLEGE_SELECTED)
	Logged_in_user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

	def __str__(self):
		return str(self.Logged_in_user)

#create new model for displaying results
class GiveResult(models.Model):
	name=models.CharField(max_length=10,default='user')
	allotted_list=models.CharField(max_length=100)
	logged_in_user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

	def __str__(self):
		return str(self.logged_in_user)		