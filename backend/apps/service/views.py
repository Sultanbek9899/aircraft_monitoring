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
    ChronicleDetailSerializer
)
from backend.apps.service.models import Event,Chronicle
from datetime import timedelta


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventSerializer


class ChronicleCreateView(generics.CreateAPIView):
    serializer_class = ChronicleSerializer


class ChroniclesListView(generics.ListAPIView):
    serializer_class = ChronicleDetailSerializer
    queryset = Chronicle.objects.all()

# class ChronicEventsList(generics.ListAPIView):
#     serializer_class = ChronicleEventsSerializer
#
#     def get_queryset(self):
#         try:
#             chronicle = Chronicle.objects.get(id=self.kwargs.get("pk"))
#         except Chronicle.DoesNotExist:
#             print("1")
#             raise Http404
#         queryset = Event.objects.filter(
#             Q(aircraft=chronicle.aircraft) & Q(unique_id=chronicle.unique_id) &
#             Q(datetime__range=(
#                 chronicle.min_timestamp,
#                 chronicle.max_timestamp
#             ))) \
#             .annotate(day=TruncDay("datetime"))\
#             .values("day")\
#             .order_by("day")\
#             .annotate(**{"total": Count("datetime")})\
#             .values("day", "total")
#         date_count = chronicle.max_timestamp.date()-chronicle.min_timestamp.date()
#         for i
#         chronicle_events = list()
#         print(date_count)
#         print(len(queryset))
#         # for day in range(0, date_count.days+2):
#         #     for q in queryset:
#         #         if q['day'] == chronicle.min_timestamp.date() + timedelta(days=day):
#         #             print(1)
#         #             chronicle_events.append(1)
#         #         else:
#         #             chronicle_events.append(0)
#         print(chronicle_events)
#         print(len(chronicle_events))
#
#         # for i in range()
#         # grouped = itertools.groupby(queryset, lambda d: d.get('datetime').strftime('%Y-%m-%d'))
#         # print([(day, len(list(this_day))) for day, this_day in grouped])
#         return queryset


class ChronicEventsList(APIView):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        try:
            chronicle = Chronicle.objects.get(id=self.kwargs.get("pk"))
        except Chronicle.DoesNotExist:
            print("1")
            raise Http404
        queryset = Event.objects.filter(
            Q(aircraft=chronicle.aircraft) & Q(unique_id=chronicle.unique_id) &
            Q(datetime__range=(
                chronicle.min_timestamp,
                chronicle.max_timestamp
            ))) \
            .annotate(day=TruncDay("datetime"))\
            .values("day")\
            .order_by("day")\
            .annotate(**{"total": Count("datetime")})\
            .values("day", "total")
        data = {}
        serializer = ChronicleSerializer(instance=chronicle)
        serializer2 = ChronicleEventsSerializer(instance=queryset, many=True)
        data.update(serializer.data)
        data.update({"chronicle_events":serializer2.data})
        return Response(data=data, status=status.HTTP_200_OK)