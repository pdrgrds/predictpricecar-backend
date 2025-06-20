from rest_framework import viewsets
from .models import PrediccionVehiculo
from .serializers import PrediccionVehiculoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .predictor import predecir_precio

class PrediccionVehiculoViewSet(viewsets.ModelViewSet):
    queryset = PrediccionVehiculo.objects.all().order_by('-created_at')
    serializer_class = PrediccionVehiculoSerializer

@api_view(['POST'])
def predecir_y_guardar(request):
    try:
        data = request.data.copy()

        # Ejecutar predicción y obtener métricas
        resultado = predecir_precio(data)
        data.update(resultado)

        # Guardar en base de datos
        serializer = PrediccionVehiculoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "resultado": resultado,
                "detalle": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
