from django.conf.urls import url
from . import views

app_name='USER_DETAILS'

urlpatterns=[
 url(r'^Fill-Academic-profile/$',views.profile_views,name='userprofile'),
 url(r'^Fill-Preferences/$',views.preferences_views,name='userpreferences'),
 url(r'^Fill-Preferences/inter/$',views.intermediate_view,name='intermediate'),
 url(r'^result/$',views.results_view,name='results'),
]