# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import QueryDict
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorsView(APIView):
    # Получить список датчиков. Выдаётся список с краткой информацией по датчикам:
    # ID, название и описание.
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)

    # Создать датчик. Указываются название и описание датчика.
    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})



class SensorIdView(APIView):
    # Получить информацию по конкретному датчику. Выдаётся полная информация по датчику:
    # ID, название, описание и список всех измерений с температурой и временем.
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        sensors = Sensor.objects.filter(id=id)
        ser = SensorDetailSerializer(sensors, many=True)
        return Response(ser.data)

    # Изменить датчик. Указываются название и описание.
    def patch(self, request, id):
        obj = Sensor.objects.get(id=id)
        serializer = SensorDetailSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)




class MeasurementView(APIView):
    # Получить список температур. Выдаётся список с краткой информацией по температурам:
    # ID датчика, temperature, date_updated
    def get(self, request):
        measurements = Measurement.objects.all()
        ser = MeasurementSerializer(measurements, many=True)
        return Response(ser.data)

    # Добавить измерение. Указываются ID датчика и температура.
    def post(self, request, *args, **kwargs):
        serializer = MeasurementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})