from django.contrib import admin
from .models import Office,TimeSlot,Desk,Room
# Register your models here.
admin.site.register(Office)
admin.site.register(TimeSlot)
admin.site.register(Desk)
admin.site.register(Room)