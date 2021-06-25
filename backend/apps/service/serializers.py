from rest_framework import serializers
from backend.apps.service.models import Event, Chronicle


class ChronicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chronicle
        fields = [
            "min_timestamp",
            "max_timestamp",
            "status",
            "aircraft",
            "unique_id"
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "datetime",
            "aircraft",
            "unique_id",
        ]


class ChronicleEventsSerializer(serializers.Serializer):
    day = serializers.DateTimeField()
    total = serializers.IntegerField()


class ChronicleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chronicle
        fields = "__all__"


class TestChronicleEventSerializer(serializers.Serializer):
    day = serializers.DateField()
    total = serializers.IntegerField