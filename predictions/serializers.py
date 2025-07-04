from rest_framework import serializers
from .models import PrediccionVehiculo
from catalogos.models import (
    MarcaVehiculo, ModeloVehiculo, VersionVehiculo,
    TipoCombustible, TipoTransmision, TipoTraccion,
    ColorVehiculo, TipoVehiculo, CondicionVehiculo
)
from catalogos.serializers import (
    MarcaVehiculoSerializer, ModeloVehiculoSerializer,
    VersionVehiculoSerializer, TipoCombustibleSerializer,
    TipoTransmisionSerializer, TipoTraccionSerializer,
    ColorVehiculoSerializer, TipoVehiculoSerializer,
    CondicionVehiculoSerializer
)

class PrediccionVehiculoSerializer(serializers.ModelSerializer):
    # — Campos de escritura (solo reciben el ID)
    brand                      = serializers.PrimaryKeyRelatedField(
                                      queryset=MarcaVehiculo.objects.all(),
                                      write_only=True
                                  )
    model                      = serializers.PrimaryKeyRelatedField(
                                      queryset=ModeloVehiculo.objects.all(),
                                      write_only=True
                                  )
    version                    = serializers.PrimaryKeyRelatedField(
                                      queryset=VersionVehiculo.objects.all(),
                                      write_only=True
                                  )
    fuel_type                  = serializers.PrimaryKeyRelatedField(
                                      queryset=TipoCombustible.objects.all(),
                                      write_only=True
                                  )
    transmission_type          = serializers.PrimaryKeyRelatedField(
                                      queryset=TipoTransmision.objects.all(),
                                      write_only=True
                                  )
    traction_type              = serializers.PrimaryKeyRelatedField(
                                      queryset=TipoTraccion.objects.all(),
                                      write_only=True
                                  )
    color                      = serializers.PrimaryKeyRelatedField(
                                      queryset=ColorVehiculo.objects.all(),
                                      write_only=True
                                  )
    vehicle_type               = serializers.PrimaryKeyRelatedField(
                                      queryset=TipoVehiculo.objects.all(),
                                      write_only=True
                                  )
    body_condition             = serializers.PrimaryKeyRelatedField(
                                      queryset=CondicionVehiculo.objects.all(),
                                      write_only=True
                                  )
    chassis_condition          = serializers.PrimaryKeyRelatedField(
                                      queryset=CondicionVehiculo.objects.all(),
                                      write_only=True
                                  )
    brakes_condition           = serializers.PrimaryKeyRelatedField(
                                      queryset=CondicionVehiculo.objects.all(),
                                      write_only=True
                                  )
    suspension_condition       = serializers.PrimaryKeyRelatedField(
                                      queryset=CondicionVehiculo.objects.all(),
                                      write_only=True
                                  )
    exhaust_system_condition   = serializers.PrimaryKeyRelatedField(
                                      queryset=CondicionVehiculo.objects.all(),
                                      write_only=True
                                  )
    air_conditioning_condition = serializers.PrimaryKeyRelatedField(
                                      queryset=CondicionVehiculo.objects.all(),
                                      write_only=True
                                  )
    electrical_system_condition= serializers.PrimaryKeyRelatedField(
                                      queryset=CondicionVehiculo.objects.all(),
                                      write_only=True
                                  )

    # — Campos de lectura (nested serializers)
    brand_info                      = MarcaVehiculoSerializer(source='brand', read_only=True)
    model_info                      = ModeloVehiculoSerializer(source='model', read_only=True)
    version_info                    = VersionVehiculoSerializer(source='version', read_only=True)
    fuel_type_info                  = TipoCombustibleSerializer(source='fuel_type', read_only=True)
    transmission_type_info          = TipoTransmisionSerializer(source='transmission_type', read_only=True)
    traction_type_info              = TipoTraccionSerializer(source='traction_type', read_only=True)
    color_info                      = ColorVehiculoSerializer(source='color', read_only=True)
    vehicle_type_info               = TipoVehiculoSerializer(source='vehicle_type', read_only=True)
    body_condition_info             = CondicionVehiculoSerializer(source='body_condition', read_only=True)
    chassis_condition_info          = CondicionVehiculoSerializer(source='chassis_condition', read_only=True)
    brakes_condition_info           = CondicionVehiculoSerializer(source='brakes_condition', read_only=True)
    suspension_condition_info       = CondicionVehiculoSerializer(source='suspension_condition', read_only=True)
    exhaust_system_condition_info   = CondicionVehiculoSerializer(source='exhaust_system_condition', read_only=True)
    air_conditioning_condition_info = CondicionVehiculoSerializer(source='air_conditioning_condition', read_only=True)
    electrical_system_condition_info= CondicionVehiculoSerializer(source='electrical_system_condition', read_only=True)

    class Meta:
        model = PrediccionVehiculo
        fields = [
            'id',
            'year_of_manufacture',
            'brand', 'brand_info',
            'model', 'model_info',
            'version', 'version_info',
            'fuel_type', 'fuel_type_info',
            'transmission_type', 'transmission_type_info',
            'traction_type', 'traction_type_info',
            'color', 'color_info',
            'vehicle_type', 'vehicle_type_info',
            'number_of_doors',
            'engine_power',
            'mileage',
            'oil_change_frequency',
            'filter_change_frequency',
            'engine_modifications',
            'critical_replacements',
            'documentation_in_order',
            'taxes_in_order',
            'technical_review_valid',
            'body_condition', 'body_condition_info',
            'chassis_condition', 'chassis_condition_info',
            'brakes_condition', 'brakes_condition_info',
            'suspension_condition', 'suspension_condition_info',
            'exhaust_system_condition', 'exhaust_system_condition_info',
            'air_conditioning_condition', 'air_conditioning_condition_info',
            'electrical_system_condition', 'electrical_system_condition_info',
            'front_image',
            'left_side_image',
            'right_side_image',
            'rear_image',
            'engine_image',
            'interior_image',
            'seats_image',
            'dashboard_image',
            'valued_amount',
            'mae',
            'squared',
            'rmse',
            'user',
            'copied_user',
            'created_at',
        ]
        read_only_fields = ['created_at']
