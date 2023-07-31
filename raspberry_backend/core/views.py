from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.generics import get_object_or_404

from django.http import JsonResponse
from .serializers import TemperatureSensorDataSerializer
from .models import TemperatureSensorData
# from json import JSONDecodeError
# Create your views here.


class TemperatureAPIView(views.APIView):
    """
    A simple APIView for creating contact entries.
    """
    serializer_class = TemperatureSensorDataSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = TemperatureSensorDataSerializer(data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "Json decoding error"}, status=400)

    def get(self, request, id=None):
        if id is not None:
            instance = get_object_or_404(TemperatureSensorData, id=id)
            serializer = TemperatureSensorDataSerializer(instance)
            return Response(serializer.data)
        else:
            connection_instance = TemperatureSensorData.objects.all()
            serializer = TemperatureSensorDataSerializer(connection_instance, many=True)
            return Response(serializer.data) 