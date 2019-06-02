from django.shortcuts import render, get_object_or_404
from .models import Meetings, MeetingMinutes, Resource, Event
from .forms import MeetingsForm, ResourceForm, EventForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def getMeetings(request):
    meetings_list=Meetings.objects.all()
    context={'meetings_list' : meetings_list}
    return render(request,'clubapp/meeting.html', context=context)

def getResource(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubapp/resource.html', {'resource_list' : resource_list})

def getEvent(request):
    event_list=Event.objects.all()
    return render(request, 'clubapp/event.html', {'event_list' : event_list})

def meetingdetail(request, id):
    meet=get_object_or_404(Meetings, pk=id)
    resourcecount=Resource.objects.filter(user_id=id).count()
    resources=Review.objects.filter(user_id= id)
    event=Event.object.filter(userid= id)
    context={
        'meet' :meet,
        'resourcecount' : resourcecount,
        'resources' : resources,
        'event' : event

    }
    return render (request, 'pythonclub/meetingdetail.html', context = context)
@login_required
def newMeeting(request):
    form=MeetingsForm
    if request.method =='POST':
        form=MeetingsForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingsForm()
    else:
        form=MeetingsForm()
    return render(request, 'clubapp/newmeeting.html', {'form': form})
@login_required
def newEvent(request):
    form=EventForm
    if request.method =='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
    else:
        form=EventForm()
    return render(request, 'clubapp/newevent.html', {'form': form})
@login_required
def newResource(request):
    form=ResourceForm
    if request.method =='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'clubapp/newresource.html', {'form': form})

def loginMessage(request):
    return render(request, 'clubapp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'clubapp/logoutmessage.html')