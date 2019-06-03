from django.conf.urls import url,include
from . import views


app_name='ACCOUNTS'

urlpatterns = [
    url(r'^login/$',views.login_view,name='login'),
    url(r'^signup/$',views.signup_view,name='signup'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^Profile/$',views.accounts_profile_view,name='accounts_profile_view'),
    url(r'^Profile/Edit/$',views.accounts_profile_edit,name='accounts_profile_edit'),
    url(r'^Profile/Edit/Change-Password$',views.change_password,name='change_password'),
]