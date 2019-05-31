from django.test import TestCase
from django.urls import reverse
from .models import MeetingMinutes, Meetings, Resource, Event
from django.contrib.auth.models import User

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