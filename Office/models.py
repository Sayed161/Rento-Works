from django.db import models
from Company.models import Company,OfficeAmenities
# Create your models here.
class Office(models.Model):
    office_name = models.CharField(max_length=200)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    time = models.CharField(max_length=400)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    Cancellation_policy=models.CharField(max_length=600)
    Guest_policy=models.CharField(max_length=600)
    capacity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='offices/')

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.DecimalField(max_digits=6,decimal_places=2)


class Room(models.Model):
    room_name = models.CharField(max_length=200)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    capacity = models.IntegerField(default=0)
    amenities = models.ManyToManyField(OfficeAmenities)
    image = models.ImageField(upload_to='room_images/')


class Desk(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    time = models.CharField(max_length=400)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    Cancellation_policy=models.CharField(max_length=600)
    Guest_policy=models.CharField(max_length=600)
    desk = models.IntegerField(default=0)
    image = models.ImageField(upload_to='desk/')