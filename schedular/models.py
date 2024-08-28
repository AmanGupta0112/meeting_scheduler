from django.db import models
from django.contrib.auth.models import User


class MeetingRoom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    organizer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="organized_meetings"
    )
    attendees = models.ManyToManyField(User, related_name="attended_meetings")
    room = models.ForeignKey(
        MeetingRoom, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title
