from django.shortcuts import render,redirect

# Create your views here.

def home_views(request):
	return render(request,'home/homepage.html')

def inst_views(request):
		return render(request,'home/instructions.html')	