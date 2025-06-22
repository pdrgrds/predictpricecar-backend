from rest_framework import viewsets
from .models import PrediccionVehiculo
from .serializers import PrediccionVehiculoSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .predictor import predecir_precio

class PrediccionVehiculoViewSet(viewsets.ModelViewSet):
    queryset = PrediccionVehiculo.objects.all().order_by('-created_at')
    serializer_class = PrediccionVehiculoSerializer

from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['POST'])
def predecir_y_guardar(request):
    try:
        parser_classes = (MultiPartParser, FormParser)
        data = dict(request.data)
        data = {k: v[0] if isinstance(v, list) else v for k, v in request.data.lists()}

        # Convertimos los valores string a sus tipos esperados
        def convertir(valor):
            if valor in ['true', 'True']:
                return True
            if valor in ['false', 'False']:
                return False
            try:
                return int(valor)
            except:
                return valor

        # Convertir valores (salvo imágenes)
        datos_para_modelo = {k: convertir(v) for k, v in data.items() if not hasattr(v, 'read')}
        resultado = predecir_precio(datos_para_modelo)

        print(resultado)

        # Unimos resultados al request original
        data['valued_amount'] = resultado['valued_amount']
        data['mae'] = resultado['mae']
        data['rmse'] = resultado['rmse']
        data['squared'] = resultado['squared']

        print(data)
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

