from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index' ),
	url(r'^homevisits/$', views.hvisits, name = 'hvisits' ),
	url(r'^outofhours/$', views.outofhours, name = 'outofhours' ),
	url(r'^chaperones/$', views.chaperones, name = 'chaperones' ),
	url(r'^leaflets/$', views.leaflets, name = 'leaflets' ),
	url(r'^newpatients/$', views.newpatients, name = 'newpatients' ),
	url(r'^vaccines/$', views.vaccines, name = 'vaccines' ),
	url(r'^carers/$', views.carers, name = 'carers' ),
	url(r'^candc/$', views.candc, name = 'candc' ),
	url(r'^equalopps/$', views.equalopps, name = 'equal opps' ),
	url(r'^datapro/$', views.datapro, name = 'datapro' ),
	url(r'^nhscon/$', views.nhscon, name = 'nhs con' ),
]