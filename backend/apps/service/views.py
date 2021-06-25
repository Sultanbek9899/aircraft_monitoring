from django.db.models import Q, Count
from django.http import Http404
from django.db.models.functions import TruncDay
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from backend.apps.service.serializers import (
    EventSerializer,
    ChronicleSerializer,
    ChronicleEventsSerializer,
    ChronicleDetailSerializer,
)
from backend.apps.service.models import Event, Chronicle
from datetime import timedelta


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventSerializer


class ChronicleCreateView(generics.CreateAPIView):
    serializer_class = ChronicleSerializer


class ChroniclesListView(generics.ListAPIView):
    serializer_class = ChronicleDetailSerializer
    queryset = Chronicle.objects.all()


class ChronicEventsList(APIView):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        try:
            chronicle = Chronicle.objects.get(id=self.kwargs.get("pk"))
        except Chronicle.DoesNotExist:
            raise Http404
        queryset = (
            Event.objects.filter(
                Q(aircraft=chronicle.aircraft)
                & Q(unique_id=chronicle.unique_id)
                & Q(datetime__range=(chronicle.min_timestamp, chronicle.max_timestamp))
            )
            .annotate(day=TruncDay("datetime"))
            .values("day")
            .order_by("day")
            .annotate(**{"total": Count("datetime")})
            .values("day", "total")
        )
        data = {}
        serializer = ChronicleSerializer(instance=chronicle)
        serializer2 = ChronicleEventsSerializer(instance=queryset, many=True)
        data.update(serializer.data)
        data.update({"chronicle_events": serializer2.data})
        return Response(data=data, status=status.HTTP_200_OK)
