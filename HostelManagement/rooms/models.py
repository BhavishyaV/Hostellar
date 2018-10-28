from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    block =models.CharField(max_length=100,null=True,blank=True)
    room_no = models.PositiveIntegerField(null=True,blank=True)
    availability = models.IntegerField(default=1)
    occupancy = models.PositiveIntegerField(null=True,blank=True)
    floor = models.PositiveIntegerField(null=True,blank=True)
    occupation_date = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (("block", "room_no"),)
    def __str__(self):
        return self.block + " " + str(self.room_no)
    def get_absolute_url(self):
        return "/room/"
    
