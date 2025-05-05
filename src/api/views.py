from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from accounts.models import CustomUser
from core.models import (FuelType, TractionType, TransmissionType,
                         VehicleBrand, VehicleCondition, VehicleModel)
from evaluations.models import Publication, VehicleEvaluation

from .serializers import (FuelTypeSerializer, PublicationSerializer,
                          RegisterSerializer, TractionTypeSerializer,
                          TransmissionTypeSerializer, VehicleBrandSerializer,
                          VehicleConditionSerializer,
                          VehicleEvaluationSerializer, VehicleModelSerializer)


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

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

class VehicleEvaluationViewSet(ModelViewSet):
    queryset = VehicleEvaluation.objects.all().select_related('brand', 'fuel_type', 'transmission_type', 'traction_type')
    serializer_class = VehicleEvaluationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.filter(status='active').select_related('vehicle_evaluation__brand')
    serializer_class = PublicationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'vehicle_evaluation__brand__name': ['exact'],
        'vehicle_evaluation__model': ['icontains'],
        'vehicle_evaluation__year_of_manufacture': ['exact', 'gte', 'lte'],
        'vehicle_evaluation__fuel_type__name': ['exact'],
        'vehicle_evaluation__transmission_type__name': ['exact'],
        'vehicle_evaluation__traction_type__name': ['exact'],
        'vehicle_evaluation__valued_amount': ['gte', 'lte'],
    }
    search_fields = ['title', 'description', 'vehicle_evaluation__model']
    ordering_fields = ['vehicle_evaluation__valued_amount', 'vehicle_evaluation__year_of_manufacture']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VehicleModelViewSet(ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer
    permission_classes = [IsAuthenticated]

class ComparePublicationsView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        ids = request.data.get("publication_ids", [])
        if not ids:
            return Response({"error": "Debe proporcionar al menos un ID."}, status=status.HTTP_400_BAD_REQUEST)

        publications = Publication.objects.filter(id__in=ids, status='active').select_related(
            'vehicle_evaluation__brand',
            'vehicle_evaluation__fuel_type',
            'vehicle_evaluation__transmission_type',
            'vehicle_evaluation__traction_type',
        )

        data = []
        for pub in publications:
            ve = pub.vehicle_evaluation
            data.append({
                "id": pub.id,
                "title": pub.title,
                "brand": ve.brand.name,
                "model": ve.model,
                "year": ve.year_of_manufacture,
                "price": float(ve.valued_amount),
                "mileage": ve.mileage,
                "fuel_type": ve.fuel_type.name,
                "transmission": ve.transmission_type.name,
                "traction": ve.traction_type.name,
                "condition": ve.body_condition.name,
                "main_image_url": pub.main_image.url if pub.main_image else None,
            })

        return Response(data, status=status.HTTP_200_OK)
