from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from .models import Event
from .forms import EventForm

# View to display all events
def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

# View to display event details using the slug

def event_detail(request, event_id):
    # Retrieve event using event_id instead of slug
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

# View for the payment page
def payment(request):
    return render(request, 'payment.html')

# View for participation page
def participate(request):
    return render(request, 'participate.html')

# Admin-only view to create an event
def create_event(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to create an event.")
        return redirect('events')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user  # Associate the event with the user
            event.save()  # Save the event without a slug
            messages.success(request, "Event created successfully!")
            return redirect('event_detail', event_id=event.id)  # Use event.id for redirection
    else:
        form = EventForm()

    return render(request, 'create_event.html', {'form': form})