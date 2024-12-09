from django import forms
from .models import Office, TimeSlot, Room, Desk

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ['office_name', 'company', 'time', 'cost', 'Cancellation_policy', 'Guest_policy', 'capacity', 'image']

class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['start_time', 'end_time', 'price']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'company', 'capacity', 'amenities', 'image']

class DeskForm(forms.ModelForm):
    class Meta:
        model = Desk
        fields = ['company', 'time', 'cost', 'Cancellation_policy', 'Guest_policy', 'desk', 'image']
