"""
Archivo principal del proyecto Predictor de Saltos.

Este archivo es el punto de entrada de la aplicación.
Su función es iniciar la interfaz gráfica del programa.

Para ejecutar el proyecto, se debe correr este archivo con:

    python main.py
"""

# Importamos la función que inicia la interfaz gráfica
from gui.app import iniciar_app


# Esta condición permite que el programa solo se ejecute
# cuando este archivo se corre directamente.
# Evita que la app se abra si el archivo es importado desde otro módulo.
if __name__ == "__main__":
    iniciar_app()