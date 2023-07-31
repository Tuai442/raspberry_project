from django.db import models

# Create your models here.
class TemperatureSensorData(models.Model):
    temperature = models.FloatField()

    def __str__(self):
        return str(self.temperature) + "°C"