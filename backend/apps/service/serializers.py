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
        model = Chronicle
        fields = [
            "datetime",
            "aircraft",
            "unique_id",
        ]