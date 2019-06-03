from django.conf.urls import url
from . import views

app_name='HELP'

urlpatterns=[
	url(r'^$',views.help_view,name='helpapp'),
]