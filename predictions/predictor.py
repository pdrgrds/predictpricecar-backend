import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

modelo = joblib.load('modelo/modelo_xgboost_autos_peru.pkl')
label_encoders = joblib.load('modelo/label_encoders_autos_peru.pkl')

FEATURES = [
    'year_of_manufacture', 'model', 'version', 'color', 'number_of_doors',
    'engine_power', 'mileage', 'oil_change_frequency', 'filter_change_frequency',
    'engine_modifications', 'critical_replacements', 'documentation_in_order',
    'taxes_in_order', 'technical_review_valid',
    'brand', 'fuel_type', 'transmission_type', 'traction_type',
    'body_condition', 'chassis_condition', 'brakes_condition', 'suspension_condition',
    'exhaust_system_condition', 'air_conditioning_condition', 'electrical_system_condition'
]

def limpiar(valor):
    if isinstance(valor, str):
        return valor.strip().lower()
    return valor

def predecir_precio(data_dict):
    entrada = {k: limpiar(v) for k, v in data_dict.items() if k in FEATURES}
    df = pd.DataFrame([entrada])

    for col in df.columns:
        if col in label_encoders:
            clases = label_encoders[col].classes_
            if df[col][0] not in clases:
                df[col] = "desconocido"
            df[col] = label_encoders[col].transform(df[col])

    y_pred = modelo.predict(df)
    y_real = y_pred  # Para demo, asumimos el real = predicho (no hay valor real aún)

    mae = mean_absolute_error(y_real, y_pred)
    rmse = mean_squared_error(y_real, y_pred, squared=False)
    r2 = r2_score(y_real, y_pred)

    return {
        "valued_amount": round(float(y_pred[0]), 2),
        "mae": round(float(mae), 4),
        "rmse": round(float(rmse), 4),
        "squared": round(float(r2), 4),
    }
