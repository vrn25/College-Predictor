from django import forms
from . import models
from .all_choices import COLLEGE_SELECTED
from django.contrib.auth.models import User

class FillProfileForm(forms.ModelForm):
	class Meta:
		model=models.FillProfile
		widgets = {
            'gender': forms.RadioSelect(attrs={'class':'radio','value':'gen'}),
            'adv_air':forms.NumberInput(attrs={'placeholder':'JEE Advanced AIR'}),
            'mains_air':forms.NumberInput(attrs={'placeholder':'JEE Mains AIR'}),
            'state' : forms.Select(attrs={'placeholder':'Select your Home State','required':'True','class':'homestate'}),
            'category' : forms.Select(attrs={'placeholder':'Select your Category','required':'True'}),
        }
		fields=['adv_air','mains_air','state','category','gender']

		def clean(self):
			print(self.cleaned_data)
			return self.cleaned_data

class FillPreferForm(forms.ModelForm):
	class Meta:
		model=models.FillPrefer
		widgets={

	'college_selected': forms.SelectMultiple(attrs={'placeholder':'Fill your preferences','id':'lstBox2', 'class':'form-control' } )
		}
		fields=['college_selected']

class ResultForm(forms.ModelForm):
	class Meta:
		model=models.GiveResult
		fields=['name','allotted_list']