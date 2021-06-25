from django.urls import path, include

from backend.apps.service import views


urlpatterns = [
    path("create_new_event/", views.EventCreateView.as_view()),
    path("create_new_chronicle/", views.ChronicleCreateView.as_view()),
    path("get_all_events_in_chronic/<int:pk>/", views.ChronicEventsList.as_view()),
    path("get_chronicle_list/", views.ChroniclesListView.as_view()),
]
