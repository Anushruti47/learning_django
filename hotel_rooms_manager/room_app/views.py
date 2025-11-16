from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

from .models import Room

def room_list(request):
    if not Room.objects.exists():
        Room.objects.create(room_number="101", room_type="Single", is_available=True, price_per_night=100.00)
        Room.objects.create(room_number="102", room_type="Double", is_available=False, price_per_night=150.00)
        Room.objects.create(room_number="103", room_type="Suite", is_available=True, price_per_night=250.00)
        Room.objects.create(room_number="104", room_type="Single", is_available=True, price_per_night=90.00)
        Room.objects.create(room_number="105", room_type="Double", is_available=True, price_per_night=140.00)
        Room.objects.create(room_number="106", room_type="Suite", is_available=False, price_per_night=300.00)
        Room.objects.create(room_number="107", room_type="Single", is_available=True, price_per_night=80.00)
    
    all_rooms=Room.objects.all()

    available_rooms=Room.objects.all().filter(is_available=True)

    rooms_by_price=Room.objects.all().order_by('price_per_night')

    suite_rooms=Room.objects.all().filter(room_type="Suite")

    context={
        'all_rooms':all_rooms,
        'available_rooms':available_rooms,
        'rooms_by_price':rooms_by_price,
        'suite_rooms':suite_rooms
    }

    return render(request,'room_list.html',context)

