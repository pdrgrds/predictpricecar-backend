from rest_framework import generics
from .models import VehicleEvaluation, Publication
from .serializers import VehicleEvaluationSerializer, PublicationSerializer

class VehicleEvaluationListView(generics.ListCreateAPIView):
    queryset = VehicleEvaluation.objects.all()
    serializer_class = VehicleEvaluationSerializer

class PublicationListView(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
