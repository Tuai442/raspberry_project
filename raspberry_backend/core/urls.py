from core.views import TemperatureAPIView
from django.urls import path    


urlpatterns = [
  path('temperature/<int:id>/', TemperatureAPIView.as_view()),
  path('temperature/', TemperatureAPIView.as_view()),

]
