"""
Archivo: generator.py

Este módulo contiene funciones auxiliares para trabajar con trazas de saltos.

Una traza es una secuencia de resultados reales de instrucciones de salto.

Ejemplo:
    ["T", "T", "N", "T", "N"]

Donde:
    T = Tomado
    N = No tomado

Funciones principales:
- generar_traza_aleatoria()
- obtener_traza_predefinida()
- analizar_traza()
"""

import random


def generar_traza_aleatoria(cantidad, probabilidad_tomado):
    """
    Genera una traza aleatoria de instrucciones de salto.

    Parámetros:
        cantidad: número total de instrucciones a generar.
        probabilidad_tomado: probabilidad de que una instrucción sea tomada.
                            Debe recibirse como decimal.
                            Ejemplo: 0.6 equivale a 60%.

    Retorna:
        Lista con valores "T" y "N".

    Ejemplo:
        generar_traza_aleatoria(10, 0.6)
        podría retornar:
        ["T", "N", "T", "T", "N", "T", "N", "T", "T", "N"]
    """

    traza = []

    for _ in range(cantidad):
        numero_aleatorio = random.random()

        if numero_aleatorio < probabilidad_tomado:
            traza.append("T")
        else:
            traza.append("N")

    return traza


def obtener_traza_predefinida(tipo):
    """
    Retorna una traza predefinida según el tipo seleccionado.

    Parámetros:
        tipo: texto con el nombre de la traza.

    Opciones disponibles:
        - Mayormente tomada
        - Mayormente no tomada
        - Alternada
        - Mixta

    Retorna:
        Lista con la traza correspondiente.
        Si el tipo no existe, retorna una lista vacía.
    """

    trazas = {
        "Mayormente tomada": ["T", "T", "T", "T", "N", "T", "T", "T"],
        "Mayormente no tomada": ["N", "N", "N", "T", "N", "N", "N", "N"],
        "Alternada": ["T", "N", "T", "N", "T", "N", "T", "N"],
        "Mixta": ["T", "T", "N", "T", "N", "N", "T", "T", "T", "N"]
    }

    return trazas.get(tipo, [])


def analizar_traza(traza):
    """
    Calcula estadísticas básicas de una traza.

    Parámetros:
        traza: lista de valores "T" y "N".

    Retorna:
        Diccionario con:
            - total
            - cantidad de tomados
            - cantidad de no tomados
            - porcentaje de tomados
            - porcentaje de no tomados
    """

    total = len(traza)

    if total == 0:
        return {
            "total": 0,
            "tomados": 0,
            "no_tomados": 0,
            "porcentaje_tomados": 0,
            "porcentaje_no_tomados": 0
        }

    tomados = traza.count("T")
    no_tomados = traza.count("N")

    porcentaje_tomados = round((tomados / total) * 100, 2)
    porcentaje_no_tomados = round((no_tomados / total) * 100, 2)

    return {
        "total": total,
        "tomados": tomados,
        "no_tomados": no_tomados,
        "porcentaje_tomados": porcentaje_tomados,
        "porcentaje_no_tomados": porcentaje_no_tomados
    }