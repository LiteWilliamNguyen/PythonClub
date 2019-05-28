from django.urls import path
from . import views

#this is a comment
urlpatterns= [
    path('',views.index, name='index'),
    path('getMeeting/', views.getMeetings, name="meeting"),
    path('getResource/', views.getResource, name="resource"),
    path('getEvent/', views.getEvent, name="event")
]