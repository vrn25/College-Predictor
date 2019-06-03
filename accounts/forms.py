from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm

class SignupForm(UserCreationForm):
	email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder':'Enter Email'}))

	class Meta:
		model=User
		fields=(
			'username',
			'password1',
			'password2',
			'first_name',
			'last_name',
			'email'
		)
		widgets={
			'username':forms.fields.TextInput(attrs={'autofocus':'autofocus','placeholder':'Enter Username'})
		}

	def __init__(self, *args, **kwargs):
		#see super method
		super(SignupForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Enter Password'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Password confirmation'})    	

        #now the form fields inherited from UserCreationForm would be validated and cleaned. In my opinion, we define save function
        #again for the newly introduced fields first_name, email etc. We save these fields to the user(from the User model)
        #we had validated then form by form.is_valid() in views and now we need to clean it. For username, password1, password2 it 
        #already done into django, So we do for other form fields. This validating and cleaning is for security purposes.

	def save(self,commit=True):
		user=super(SignupForm, self).save(commit=False)
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']

		if commit:
			user.save()

		return user   # returns the user with all the form fields included in it,i.e fields inside built in UserCreationForm and also
		#new ones introduced in SignupForm. 



class LoginForm(AuthenticationForm):

	class Meta:
		model=User
		fields=(
			'username',
			'password',
			'first_name',
			'last_name',
			'email',
		)

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={ 'autofocus':'autofocus','placeholder': 'Enter Username'})
		self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Enter Password'})    	

        

	def save(self,commit=True):
		user=super(LoginForm, self).save(commit=False)
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']

		if commit:
			user.save()

		return user


class EditProfileForm(UserChangeForm):
	class Meta:
		model=User
		fields=(
			'username',
			'email',
			'password'
			)
	