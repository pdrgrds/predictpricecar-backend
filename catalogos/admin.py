from django.contrib import admin
from .models import MarcaVehiculo, ModeloVehiculo, VersionVehiculo, TipoCombustible, TipoTransmision, TipoTraccion, CondicionVehiculo, ColorVehiculo, TipoVehiculo

admin.site.register(MarcaVehiculo)
admin.site.register(ModeloVehiculo)
admin.site.register(VersionVehiculo)
admin.site.register(TipoCombustible)
admin.site.register(TipoTransmision)
admin.site.register(TipoTraccion)
admin.site.register(CondicionVehiculo)
admin.site.register(ColorVehiculo)
admin.site.register(TipoVehiculo)