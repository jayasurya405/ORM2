from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_name = models.CharField()
    car_model = models.CharField()
    release_date = models.DateField()
    mileage = models.CharField()
    color = models.CharField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'release_date', 'mileage', 'color')
# Create your models here.
