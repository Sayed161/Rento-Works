from django.shortcuts import render, redirect
from .forms import OfficeForm, TimeSlotForm, RoomForm, DeskForm
from .models import Office, TimeSlot, Room, Desk

# View for creating an Office
def create_office(request):
    if request.method == 'POST':
        form = OfficeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('office')  # Redirect to list or another view
    else:
        form = OfficeForm()
    return render(request, 'create_office.html', {'form': form})

def create_timeslot(request):
    if request.method == 'POST':
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to list or another view
    else:
        form = TimeSlotForm()
    return render(request, 'create_timeslot.html', {'form': form})

# View for creating a Room
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to list or another view
    else:
        form = RoomForm()
    return render(request, 'create_room.html', {'form': form})

# View for creating a Desk
def create_desk(request):
    if request.method == 'POST':
        form = DeskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('desk_list')  # Redirect to list or another view
    else:
        form = DeskForm()
    return render(request, 'create_desk.html', {'form': form})

# View for listing all Offices
def office_list(request):
    offices = Office.objects.all()
    return render(request, 'office_list.html', {'offices': offices})

# View for listing all TimeSlots
def timeslot_list(request):
    timeslots = TimeSlot.objects.all()
    return render(request, 'timeslot_list.html', {'timeslots': timeslots})

# View for listing all Rooms
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

# View for listing all Desks
def desk_list(request):
    desks = Desk.objects.all()
    return render(request, 'desk_list.html', {'desks': desks})
