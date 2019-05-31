from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meetings(models.Model):
    meetingtitle = models.CharField(max_length= 255)
    meetingdate = models.DateField()
    meetingtime = models.DateTimeField()
    meetinglocation = models.CharField(max_length= 255)
    meetingAgenda = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table = 'Meeting'
        verbose_name_plural="Meetings"
    

class MeetingMinutes(models.Model):
    meeting_id = models.ForeignKey(Meetings, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutetext = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meeting_id

    class Meta:
        db_table = 'Meeting Minute'
    

class Resource(models.Model):
    resourcename = models.CharField(max_length = 255)
    resourcetype = models.CharField(max_length = 255)
    resourceurl = models.URLField(null=True,blank=True)
    resourcedateenter = models.DateField()
    user_id = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    resourcedescription = models.TextField(null=True, blank=True)

    def __str__(self):
        return self. resourcename
    
    class Meta:
        db_table = 'resource'
 

class Event(models.Model):
    eventtitle = models.CharField(max_length = 255)
    eventlocation = models.CharField(max_length= 255)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    eventdescription = models.TextField(null=True,blank=True)
    userid = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table = 'event'
        verbose_name_plural = 'events'
