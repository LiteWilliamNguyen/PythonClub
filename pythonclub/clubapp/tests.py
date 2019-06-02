from django.test import TestCase
from django.urls import reverse
from .models import MeetingMinutes, Meetings, Resource, Event
from django.contrib.auth.models import User
from .forms import MeetingsForm, ResourceForm, EventForm
import datetime
# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        type=Meetings(meetingtitle="Seattle")
        self.assertEqual(str(type),type.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meetings._meta.db_table), 'Meeting')

class ResourceTest(TestCase):
    def setUp(self):
        type=Resource(resourcename='chair')

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')
    
class EventTest(TestCase):
    def setUp(self):
        event=Event(eventtitle='Seattle World Cup')

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class Meeting_Form_Test(TestCase):
    def setUp(self):
        self.user=User.objects.create(username="user1", password="P@ssw0rd1")
        self.meet=Meetings.objects.create(meetingtitle='title1',)


class Resource_Form_Test(TestCase):
    def setUp(self):
        self.user=User.objects.create(username="user1", password="P@ssw0rd1")

    def test_ResourceForm(self):
        data={
            'resourcename': 'name1',
            'resourcetype': 'some type',
            'resourceurl': 'some url',
            'resourcedateenter': datetime.datetime.now(),
            'user_id': self.user,
            'resourcedescription' : 'some description'
        }
        form=ResourceForm(data=data)
        self.assertTrue(form.is_valid)