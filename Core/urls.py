from django.urls import path
from .views import home,office,room,desk_list


urlpatterns = [
    path('', home, name='home'),
    path('office/',office, name='office'),
    path('room/',room, name='room'),
    path('desk/',desk_list, name='desk')
]