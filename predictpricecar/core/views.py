from rest_framework import generics
from .models import VehicleBrand, FuelType, TransmissionType, TractionType, VehicleCondition
from .serializers import (
    VehicleBrandSerializer,
    FuelTypeSerializer,
    TransmissionTypeSerializer,
    TractionTypeSerializer,
    VehicleConditionSerializer
)

class VehicleBrandListView(generics.ListCreateAPIView):
    queryset = VehicleBrand.objects.all()
    serializer_class = VehicleBrandSerializer

class VehicleBrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleBrand.objects.all()
    serializer_class = VehicleBrandSerializer

class FuelTypeListView(generics.ListCreateAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer

class FuelTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer

class TransmissionTypeListView(generics.ListCreateAPIView):
    queryset = TransmissionType.objects.all()
    serializer_class = TransmissionTypeSerializer

class TransmissionTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransmissionType.objects.all()
    serializer_class = TransmissionTypeSerializer

class TractionTypeListView(generics.ListCreateAPIView):
    queryset = TractionType.objects.all()
    serializer_class = TractionTypeSerializer

class TractionTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TractionType.objects.all()
    serializer_class = TractionTypeSerializer

class VehicleConditionListView(generics.ListCreateAPIView):
    queryset = VehicleCondition.objects.all()
    serializer_class = VehicleConditionSerializer

class VehicleConditionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleCondition.objects.all()
    serializer_class = VehicleConditionSerializer
