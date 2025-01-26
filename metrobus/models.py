from django.db import models

# Create your models here.

# class Service(models.Model):
#     id = models.AutoField(primary_key=True)
#     service_id = models.CharField(max_length=50)
#     monday = models.BooleanField()
#     tuesday = models.BooleanField()
#     wednesday = models.BooleanField()
#     thursday = models.BooleanField()
#     friday = models.BooleanField()
#     saturday = models.BooleanField()
#     sunday = models.BooleanField()
#     start_date = models.DateField()
#     end_date = models.DateField()

#     def __str__(self):
#         return self.service_id
    
# class Route(models.Model):
#     id = models.AutoField(primary_key=True)
#     route_id = models.CharField(max_length=50)
#     agency_id = models.CharField(max_length=50)
#     route_short_name = models.CharField(max_length=10)
#     route_long_name = models.CharField(max_length=250)
#     route_url = models.CharField(max_length=250)
#     route_color = models.CharField(max_length=10)

#     def __str__(self):
#         return self.route_id

# class Stop(models.Model):
#     id = models.AutoField(primary_key=True)
#     stop_id = models.CharField(max_length=50)
#     #stop_code = models.CharField(max_length=50)
#     stop_name = models.CharField(max_length=250)
#     #stop_desc = models.CharField(max_length=250)
#     stop_lat = models.FloatField()
#     stop_lon = models.FloatField()

#     def __str__(self):
#         return self.stop_id

# class Shape(models.Model):
#     id = models.AutoField(primary_key=True)
#     shape_id = models.CharField(max_length=50)
#     shape_pt_lat = models.FloatField()
#     shape_pt_lon = models.FloatField()
#     shape_pt_sequence = models.IntegerField()

#     def __str__(self):
#         return self.shape_id

class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    trip_id = models.CharField(max_length=50)
    trip_headsign = models.CharField(max_length=50)
    #route_id = models.ForeignKey(Route, related_name='trips', on_delete=models.CASCADE)
    #service = models.ForeignKey(Service, related_name='trips', on_delete=models.CASCADE)
    #shape = models.ForeignKey(Shape, related_name='trips', on_delete=models.CASCADE)

    def __str__(self):
        return self.trip_id
    
class StopTime(models.Model):
    id = models.AutoField(primary_key=True)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    stop_sequence = models.IntegerField()
    trip = models.ForeignKey(Trip, related_name='stoptimes', on_delete=models.CASCADE)
    #stop = models.ForeignKey(Stop, related_name='stoptimes', on_delete=models.CASCADE)

    def __str__(self):
        return self.stoptime_id
    
