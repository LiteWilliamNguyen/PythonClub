from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PythonType(models.Model):
    pythontypename = models.CharField(max_length=255)
    pythondescription = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.pythontypename
    
    class Meta:
        db_table = 'pythontype'
        verbose_name_plural = 'pythontypes'

class MeetingMinute(models.Model):
    meetingid = models.ForeignKey(PythonType, on_delete = models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutetext = models.TextField()

    def __str__(self):
        return self.meetingid

    class Meta:
        db_table = 'Meeting'
        verbose_name_plural = 'Meetings'

class Resource(models.Model):
    resourcename = models.CharField(max_length = 255)
    resourcetype = models.ForeignKey(PythonType, on_delete= models.DO_NOTHING)
    resourceurl = models.URLField(null=True,blank=True)
    resourcedateenter = models.DateField()
    userid = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    resourcedescription = models.TextField(null=True, blank=True)

    def __str__(self):
        return self. resourcename
    
    class Meta:
        db_table = 'resoure'
        verbose_name_plural = 'resources'

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
