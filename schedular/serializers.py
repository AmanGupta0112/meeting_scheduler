from rest_framework import serializers
from .models import Meeting, MeetingRoom


class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ["id", "name", "capacity"]


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = [
            "id",
            "title",
            "start_time",
            "end_time",
            "organizer",
            "attendees",
            "room",
        ]

    def validate(self, data):
        # Check for time conflicts
        conflicting_meetings = Meeting.objects.filter(
            start_time__lt=data["end_time"], end_time__gt=data["start_time"]
        )

        if self.instance:
            conflicting_meetings = conflicting_meetings.exclude(pk=self.instance.pk)

        if conflicting_meetings.exists():
            raise serializers.ValidationError(
                "There is a time conflict with another meeting."
            )

        # Check room availability
        if data.get("room"):
            room_conflicts = conflicting_meetings.filter(room=data["room"])
            if room_conflicts.exists():
                raise serializers.ValidationError(
                    "The selected room is not available at this time."
                )

        # Check attendee availability
        if "attendees" in data:
            attendee_conflicts = conflicting_meetings.filter(
                attendees__in=data["attendees"]
            )
            if attendee_conflicts.exists():
                raise serializers.ValidationError(
                    "One or more attendees are not available at this time."
                )

        return data
