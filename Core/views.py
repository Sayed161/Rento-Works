from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Company.models import RoleRequest
from Office.models import Office,Desk,Room,TimeSlot
# Create your views here.
def home(request):
     approved_role_requests = RoleRequest.objects.filter(status='approved')
     for role_request in approved_role_requests:
        role_request.approve() 
     return render(request, 'home.html')

def office(request):
     offices = Office.objects.all() 
     return render(request, 'office.html', {'office': offices})

def room(request):
     rooms = Room.objects.all()
     slot = TimeSlot.objects.all()
     return render(request, 'room.html', {'room': rooms,'slot': slot})

def desk_list(request):
    desks = Desk.objects.all()
    return render(request, 'desk_list.html', {'desks': desks})