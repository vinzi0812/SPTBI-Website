from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('incubation/', incubation, name='incubation'),
    path('virtualincubation/', virtualincubation, name='virtualincubation'),
    path('team/', team, name='team'),
    path('meetingroom/', meetingroom, name='meetingroom'),
    path('login/', loginuser, name='login'),
    path('mentors/', mentors, name='mentors'),
    path('logout/', logoutuser, name='logout'),
    path('currentincubatee/', currentincubatee, name='currentincubatee'),
    path('graduatedincubatee/', graduatedincubatee, name='graduatedincubatee'),
    path('programme/<slug:page_slug>/', pgtemplate, name='programme'),
    path('cabinspace/', cabinspace, name='cabinspace'),
    path('labs/', labs, name='labs'),
    path('iot/', iot, name='iot'),
    path('events/<slug:page_slug>', events, name='events'),
]