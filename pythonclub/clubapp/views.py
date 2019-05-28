from django.shortcuts import render, get_object_or_404
from .models import Meetings, MeetingMinutes, Resource, Event



# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def getMeetings(request):
    meetings_list=Meetings.objects.all()
    context={'meetings_list' : types_list}
    return render(request,'clubapp/types.html', context=context)

def getResource(request):
    resouce_list=Resource.objects.all()
    return render(request, 'clubapp/resource.html',{'resource_list' : resource_list})

