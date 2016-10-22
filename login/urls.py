from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^create_profile/$', views.create_profile, name='create_profile'),
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<user_id>[0-9]+)/update_profile/$', views.update_profile, name='update_profile'),
    url(r'^book/', views.book, name='book'),
    url(r'^view/', views.view, name='view'),
    url(r'^staff/', views.staff, name='staff'),
]
