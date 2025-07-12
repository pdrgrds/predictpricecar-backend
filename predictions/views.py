from rest_framework import viewsets
from .models import PrediccionVehiculo
from .serializers import PrediccionVehiculoSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from .predictor import predecir_precio
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from blog.models import BlogPost
from django.db.models import Q
from catalogos.models import (
    MarcaVehiculo,
    ColorVehiculo,
    TipoCombustible,
    TipoTransmision
)
from django.db import models


class PrediccionVehiculoViewSet(viewsets.ModelViewSet):
    queryset = PrediccionVehiculo.objects.all().order_by('-created_at')
    serializer_class = PrediccionVehiculoSerializer

class UserPredictionsListAPIView(APIView):
    """
    Lista todas las predicciones del usuario autenticado
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        predictions = PrediccionVehiculo.objects.filter(user=request.user).order_by("-created_at")
        results = []
        for pred in predictions:
            # Buscar si hay un blog vinculado
            blog = BlogPost.objects.filter(prediction=pred).first()
            results.append({
                "id": pred.id,
                "brand": pred.brand.name if pred.brand else None,
                "model": pred.model.name if pred.model else None,
                "year_of_manufacture": pred.year_of_manufacture,
                "valued_amount": pred.valued_amount,
                "created_at": pred.created_at,
                "idPublish": blog.id if blog else None
            })
        return Response(results, status=status.HTTP_200_OK)

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

class ListPrediccionesFilteredAPIView(APIView):
    """
    API para listar predicciones con filtros opcionales
    """

    def get(self, request):
        qs = PrediccionVehiculo.objects.all().select_related(
            "brand", "model", "version", "fuel_type", "transmission_type", "color"
        )

        # Filtros
        marca = request.query_params.get("marca")
        precio_min = request.query_params.getlist("precio")[0] if "precio" in request.query_params else None
        precio_max = request.query_params.getlist("precio")[1] if "precio" in request.query_params else None
        km_min = request.query_params.getlist("kilometraje")[0] if "kilometraje" in request.query_params else None
        km_max = request.query_params.getlist("kilometraje")[1] if "kilometraje" in request.query_params else None
        anio_min = request.query_params.getlist("anio")[0] if "anio" in request.query_params else None
        anio_max = request.query_params.getlist("anio")[1] if "anio" in request.query_params else None
        combustible = request.query_params.getlist("combustible")
        transmision = request.query_params.getlist("transmision")
        color = request.query_params.get("color")

        if marca:
            qs = qs.filter(brand_id=marca)
        if precio_min and precio_max:
            qs = qs.filter(valued_amount__gte=precio_min, valued_amount__lte=precio_max)
        if km_min and km_max:
            qs = qs.filter(mileage__gte=km_min, mileage__lte=km_max)
        if anio_min and anio_max:
            qs = qs.filter(year_of_manufacture__gte=anio_min, year_of_manufacture__lte=anio_max)
        if combustible:
            qs = qs.filter(fuel_type_id__in=combustible)
        if transmision:
            qs = qs.filter(transmission_type_id__in=transmision)
        if color:
            qs = qs.filter(color_id=color)

        data = [
            {
                "id": pred.id,
                "brand": pred.brand.name if pred.brand else "",
                "model": pred.model.name if pred.model else "",
                "version": pred.version.name if pred.version else "",
                "mileage": pred.mileage,
                "fuel_type": pred.fuel_type.name if pred.fuel_type else "",
                "transmission_type": pred.transmission_type.name if pred.transmission_type else "",
                "valued_amount": pred.valued_amount,
                "front_image": request.build_absolute_uri(pred.front_image.url) if pred.front_image else None,
            }
            for pred in qs.order_by("-created_at")
        ]
        return Response(data, status=status.HTTP_200_OK)

class PredictionFiltersAPIView(APIView):
    """
    API que devuelve los datos necesarios para filtros de predicciones.
    """

    def get(self, request):
        # Precios
        prices = PrediccionVehiculo.objects.aggregate(
            min_price=models.Min("valued_amount"),
            max_price=models.Max("valued_amount")
        )
        # Kilometraje
        mileage = PrediccionVehiculo.objects.aggregate(
            min_mileage=models.Min("mileage"),
            max_mileage=models.Max("mileage")
        )
        # Año de fabricación
        years = PrediccionVehiculo.objects.aggregate(
            min_year=models.Min("year_of_manufacture"),
            max_year=models.Max("year_of_manufacture")
        )
        # Listados
        brands = MarcaVehiculo.objects.values("id", "name")
        colors = ColorVehiculo.objects.values("id", "name")
        fuels = TipoCombustible.objects.values("id", "name")
        transmissions = TipoTransmision.objects.values("id", "name")

        return Response({
            "brand": list(brands),
            "amount_price": [prices["min_price"], prices["max_price"]],
            "mileage": [mileage["min_mileage"], mileage["max_mileage"]],
            "year_vehicle": [years["min_year"], years["max_year"]],
            "fuel_type": list(fuels),
            "transmission_type": list(transmissions),
            "color": list(colors)
        })
