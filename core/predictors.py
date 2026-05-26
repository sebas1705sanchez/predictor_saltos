"""
Archivo: predictors.py

Este módulo contiene las clases que representan los diferentes
predictores de saltos utilizados en el programa.

Cada predictor implementa dos métodos principales:
- predecir(): retorna 'T' o 'N'
- actualizar(): ajusta el estado interno según el resultado real

Tipos de predictores implementados:
1. Predict Not Taken (Siempre predice N)
2. Predict Taken (Siempre predice T)
3. Predictor de 2 bits (Dinámico, aprende del comportamiento)
"""


class PredictorNotTaken:
    """
    Predictor estático que siempre predice que el salto NO se toma.
    """

    def __init__(self):
        self.nombre = "Predict Not Taken"

    def predecir(self):
        """
        Retorna siempre 'N' (No tomado)
        """
        return "N"

    def actualizar(self, resultado_real):
        """
        Este predictor no aprende, por lo tanto no hace nada.
        """
        pass


class PredictorTaken:
    """
    Predictor estático que siempre predice que el salto SI se toma.
    """

    def __init__(self):
        self.nombre = "Predict Taken"

    def predecir(self):
        """
        Retorna siempre 'T' (Tomado)
        """
        return "T"

    def actualizar(self, resultado_real):
        """
        No tiene aprendizaje.
        """
        pass


class Predictor2Bits:
    """
    Predictor dinámico basado en una máquina de estados de 2 bits.

    Estados posibles:
        0 = Fuertemente No Tomado
        1 = Débilmente No Tomado
        2 = Débilmente Tomado
        3 = Fuertemente Tomado

    Regla:
        - Si estado >= 2 → predice T
        - Si estado < 2 → predice N

    Aprende del comportamiento ajustando su estado.
    """

    def __init__(self):
        self.nombre = "Predictor de 2 Bits"

        # Estado inicial (débilmente no tomado)
        self.estado = 1

    def predecir(self):
        """
        Realiza la predicción basada en el estado actual.
        """
        if self.estado >= 2:
            return "T"
        else:
            return "N"

    def actualizar(self, resultado_real):
        """
        Actualiza el estado del predictor según el resultado real.

        Si el salto fue tomado (T):
            incrementa el estado (máximo 3)

        Si el salto NO fue tomado (N):
            decrementa el estado (mínimo 0)
        """

        if resultado_real == "T":
            if self.estado < 3:
                self.estado += 1

        elif resultado_real == "N":
            if self.estado > 0:
                self.estado -= 1

    def nombre_estado(self):
        """
        Retorna el nombre del estado actual en texto.
        Sirve para visualización o debugging.
        """

        estados = {
            0: "Fuertemente No Tomado",
            1: "Débilmente No Tomado",
            2: "Débilmente Tomado",
            3: "Fuertemente Tomado"
        }

        return estados[self.estado]