from django.urls import path
from . import views

#this is a comment
urlpatterns= [
    path('',views.index, name='index'),
    path('getMeeting/', views.getMeetings, name="meeting"),
    path('getResource/', views.getResource, name="resource"),
    path('getEvent/', views.getEvent, name="event"),
    path('newMeeting/', views.newMeeting, name="newmeeting"),
    path('loginmessage/',views.loginMessage, name='loginmessage'),
    path('logoutmessasge/', views.logoutMessage, name="logoutmessage")
]