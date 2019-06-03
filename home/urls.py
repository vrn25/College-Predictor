from django.conf.urls import url
from . import views

app_name='HOME'

urlpatterns=[
 url(r'^$',views.home_views,name='homepage'),
 url(r'^instructions/$',views.inst_views,name='inst'),
]