from datetime import datetime
from django.shortcuts import render
from .models import Event,Registration

# Create your views here.
def home(request):
    # Add sample data if DB is empty
    if Event.objects.count() == 0:
        e1 = Event.objects.create(name="Tech Conference", description="Annual tech event", fee=100, is_online=False)
        e2 = Event.objects.create(name="Art Expo", description="Explore art", fee=50, is_online=True)

        Registration.objects.create(event=e1, participant_name="Alice", participant_email="alice@example.com", number_of_tickets=2, registered_at=datetime(2024, 7, 1, 10, 0))
        Registration.objects.create(event=e1, participant_name="Bob", participant_email="bob@example.com", number_of_tickets=1, registered_at=datetime(2024, 7, 1, 11, 30))
        Registration.objects.create(event=e2, participant_name="Charlie", participant_email="charlie@example.com", number_of_tickets=3, registered_at=datetime(2024, 7, 2, 15, 0))

    events = Event.objects.all().prefetch_related('registrations')

    return render(request,"home.html",{'events':events})

