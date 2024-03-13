from datetime import datetime

from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    date_updated = models.DateTimeField(auto_now=True)
    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    def save_date(self):
        self.date_updated = datetime.datetime.now()






