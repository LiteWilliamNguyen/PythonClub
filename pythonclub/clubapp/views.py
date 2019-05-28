from django.shortcuts import render, get_object_or_404
from .models import Meetings, MeetingMinutes, Resource, Event
from .forms import MeetingsForm, ResourceForm, EventForm


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

def getEvent(request):
    event_list=Event.object.all()
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

def newProduct(request):
    form=ProductForm
    if request.method =='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ProductForm()
    else:
        form=ProductForm()
    return render(request, 'TechReviewApp/newproduct.html', {'form': form})

def newReview(request):
    form=ReviewForm
    if request.method =='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'TechReviewApp/newreview.html', {'form': form})
