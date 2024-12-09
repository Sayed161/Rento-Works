from django.urls import path
from . import views

urlpatterns = [
    path('create_office/', views.create_office, name='create_office'),
    path('create_timeslot/', views.create_timeslot, name='create_timeslot'),
    path('create_room/', views.create_room, name='create_room'),
    path('create_desk/', views.create_desk, name='create_desk'),
    path('office_list/', views.office_list, name='office_list'),
    path('timeslot_list/', views.timeslot_list, name='timeslot_list'),
    path('room_list/', views.room_list, name='room_list'),
    path('desk_list/', views.desk_list, name='desk_list'),
]
