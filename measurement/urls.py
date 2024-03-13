from django.urls import path

from measurement.views import SensorsView, MeasurementView, SensorIdView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<int:id>/', SensorIdView.as_view()),
]
