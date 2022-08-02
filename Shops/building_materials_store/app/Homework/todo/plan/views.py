from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
)
from django.urls import reverse

from .forms import EventForm
from .models import Event


class EventCreateView(CreateView):
    template_name: str = "plan/event_add.html"
    form_class: type = EventForm

    def get_success_url(self):
        return reverse('event-list')


class EventListView(ListView):
    template_name: str = "plan/event_list.html"
    model: type = Event

    def get_queryset(self):
        status = self.request.GET.get("status")
        result = Event.objects.all()
        if status:
            result = Event.objects.filter(status=status)
        return result


class EventDetailView(DetailView):
    template_name: str = "plan/event_detail.html"
    model: type = Event


class EventDeleteView(DeleteView):
    template_name: str = "plan/event_delete.html"
    model: type = Event
    success_url: str = "#"

    def get_success_url(self):
        return reverse('event-list')


class EventUpdateView(UpdateView):
    template_name: str = "plan/event_update.html"
    form_class: type = EventForm
    model = Event

    def get_success_url(self):
        return reverse('event-list')
