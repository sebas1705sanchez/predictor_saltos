"""
Archivo: evaluator.py

Este módulo se encarga de evaluar el rendimiento de los predictores
de saltos comparando sus predicciones con una traza real.

Funciones principales:
- evaluar_predictor(): evalúa un predictor individual
- comparar_predictores(): compara todos los predictores

Se calcula:
- Número de aciertos
- Total de instrucciones
- Tasa de aciertos (%)
- Historial detallado de cada instrucción
"""

# Importamos los predictores
from core.predictors import PredictorNotTaken, PredictorTaken, Predictor2Bits


def evaluar_predictor(predictor, traza):
    """
    Evalúa un predictor con respecto a una traza de saltos.

    Parámetros:
        predictor: instancia de un predictor (objeto)
        traza: lista de caracteres ['T', 'N', ...]

    Retorna:
        diccionario con:
            - nombre del predictor
            - aciertos
            - total de instrucciones
            - tasa de aciertos
            - historial detallado
    """

    aciertos = 0
    historial = []

    # Recorremos cada instrucción de la traza
    for i, resultado_real in enumerate(traza, start=1):

        # El predictor hace una predicción
        prediccion = predictor.predecir()

        # Verificamos si acertó
        acierto = prediccion == resultado_real

        if acierto:
            aciertos += 1

        # Si es el predictor de 2 bits, obtenemos su estado
        estado_2_bits = (
            predictor.nombre_estado()
            if isinstance(predictor, Predictor2Bits)
            else "No aplica"
        )

        # Guardamos el detalle de esta instrucción
        historial.append({
            "Instrucción": i,
            "Predictor": predictor.nombre,
            "Predicción": prediccion,
            "Real": resultado_real,
            "Resultado": "Acierto" if acierto else "Fallo",
            "Estado 2 Bits": estado_2_bits
        })

        # Actualizamos el predictor (aprendizaje)
        predictor.actualizar(resultado_real)

    total = len(traza)

    # Calculamos la tasa de aciertos
    tasa = (aciertos / total) * 100 if total > 0 else 0

    # Retornamos todos los resultados
    return {
        "predictor": predictor.nombre,
        "aciertos": aciertos,
        "total": total,
        "tasa": round(tasa, 2),
        "historial": historial
    }


def comparar_predictores(traza):
    """
    Compara todos los predictores disponibles usando la misma traza.

    Parámetros:
        traza: lista de 'T' y 'N'

    Retorna:
        - lista de resultados resumidos
        - historial completo combinado
    """

    # Creamos instancias de cada predictor
    predictores = [
        PredictorNotTaken(),
        PredictorTaken(),
        Predictor2Bits()
    ]

    resultados = []
    historial_total = []

    # Evaluamos cada predictor
    for predictor in predictores:

        resultado = evaluar_predictor(predictor, traza)

        # Guardamos resumen
        resultados.append({
            "Predictor": resultado["predictor"],
            "Aciertos": resultado["aciertos"],
            "Total": resultado["total"],
            "Tasa de aciertos (%)": resultado["tasa"]
        })

        # Guardamos historial detallado
        historial_total.extend(resultado["historial"])

    return resultados, historial_total