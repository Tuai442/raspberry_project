from rest_framework import serializers
from .models import TemperatureSensorData

class TemperatureSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureSensorData
        fields = ['temperature']