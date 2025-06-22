import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Cargar modelo y encoders
modelo = joblib.load('modelo/modelo_xgboost_autos_peru.pkl')
label_encoders = joblib.load('modelo/label_encoders_autos_peru.pkl')

# Lista de columnas usadas por el modelo (actualizada con vehicle_type)
FEATURES = [
    'year_of_manufacture', 'model', 'version', 'color', 'number_of_doors',
    'engine_power', 'mileage', 'oil_change_frequency', 'filter_change_frequency',
    'engine_modifications', 'critical_replacements', 'documentation_in_order',
    'taxes_in_order', 'technical_review_valid',
    'brand', 'fuel_type', 'transmission_type', 'traction_type',
    'body_condition', 'chassis_condition', 'brakes_condition', 'suspension_condition',
    'exhaust_system_condition', 'air_conditioning_condition', 'electrical_system_condition',
    'vehicle_type'
]

def limpiar(valor):
    if isinstance(valor, bool):
        return str(valor)
    if isinstance(valor, str):
        return valor.strip().lower()
    return valor

def predecir_precio(data_dict):
    # Preparar DataFrame
    entrada = {k: limpiar(v) for k, v in data_dict.items() if k in FEATURES}
    df = pd.DataFrame([entrada])

    # Aplicar encoders si existen
    for col in df.columns:
        if col in label_encoders:
            le = label_encoders[col]
            valor = str(df[col][0])
            if valor not in le.classes_:
                # Evitar error si 'desconocido' no está en las clases
                if "desconocido" in le.classes_:
                    df[col] = "desconocido"
                else:
                    raise ValueError(f"❌ El valor '{valor}' en la columna '{col}' no es reconocido por el modelo.")
            df[col] = le.transform(df[col])

    if hasattr(modelo, "feature_names_in_"):
        df = df[modelo.feature_names_in_]
    else:
        df = df[FEATURES]

    # Predecir
    y_pred = modelo.predict(df)

    # Evaluación simulada (ya que no se conoce el real)
    mae = 0#mean_absolute_error(y_pred, y_pred)
    rmse = 0#mean_squared_error(y_pred, y_pred)
    r2 = 0#r2_score(y_pred, y_pred)


    return {
        "valued_amount": round(float(y_pred[0]), 2),
        "mae": round(float(mae), 2),
        "rmse": round(float(rmse), 2),
        "squared": round(float(r2), 2),
    }
