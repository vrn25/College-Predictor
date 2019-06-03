from django.shortcuts import render,redirect
from . import forms
from accounts.forms import SignupForm, LoginForm, EditProfileForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def login_view(request):
	msg=""
	if request.method=='POST':
		form=LoginForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('USER_DETAILS:userprofile')
		else:
			msg="LOGIN FAILED! TRY AGAIN"
	else:
		form=LoginForm()
	return render(request,'accounts/login2.html',{'loginform':form,'msg':msg})

def signup_view(request):
	if request.method=='POST':
		form=forms.SignupForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('USER_DETAILS:userprofile')
	else:
		form=forms.SignupForm()
	return render(request,'accounts/signup.html',{'signupform': form})


def logout_view(request):
	logout(request)
	return render(request,'accounts/logout.html')

@login_required(login_url='ACCOUNTS:login')
def accounts_profile_view(request):
	args={'accounts_profile_form':request.user}
	return render(request,'accounts/view_account_profile.html',args)

@login_required(login_url='ACCOUNTS:login')
def accounts_profile_edit(request):
	if request.method=='POST':
		form=EditProfileForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('ACCOUNTS:accounts_profile_view')
	else:
		form=EditProfileForm(instance=request.user)
	args={'accounts_edit_form_custom':form}
	return render(request,'accounts/edit_account_profile.html',args)

@login_required(login_url='ACCOUNTS:login')
def change_password(request):
	if request.method=='POST':
		form=PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('ACCOUNTS:accounts_profile_view')
	else:
		form=PasswordChangeForm(user=request.user)
	args={'accounts_edit_form_custom':form}
	return render(request,'accounts/change_password.html',args)