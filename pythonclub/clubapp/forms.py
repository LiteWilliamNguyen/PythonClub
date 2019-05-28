from django import forms
from .models import MeetingMinutes, Meetings, Resource, Event

class MeetingsForm(forms.ModelForm):
    class Meta:
        model=Meetings
        fields='__all__'

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"