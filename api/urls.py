from django.urls import path
from .views import PortFolioAPI
urlpatterns = [
    path('api/', PortFolioAPI.as_view(),name="apiview"),
]
