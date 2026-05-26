# Predictor de Saltos

Proyecto académico desarrollado en Python para comparar estrategias de predicción de saltos en arquitectura de computadores.

El sistema permite evaluar tres estrategias:

1. **Predict Not Taken**
2. **Predict Taken**
3. **Predictor de 2 Bits**

La comparación se realiza usando trazas de instrucciones de salto. Cada instrucción puede representar si un salto fue tomado o no tomado.

---

## Contexto

En los procesadores segmentados mediante *pipeline*, las instrucciones de salto pueden generar riesgos de control. Esto ocurre porque el procesador no siempre sabe de inmediato cuál será la siguiente instrucción que debe ejecutar.

La predicción de saltos busca anticipar el comportamiento de una instrucción de salto para reducir pérdidas de ciclos y mejorar el rendimiento del procesador.

Este proyecto simula ese comportamiento de forma didáctica, comparando diferentes estrategias de predicción y midiendo su tasa de aciertos.

---

## Objetivo

Comparar el rendimiento de tres estrategias de predicción de saltos mediante distintas trazas de instrucciones, calculando la cantidad de aciertos y la tasa de precisión de cada predictor.

---

## Funcionalidades

- Comparación entre tres predictores de saltos.
- Uso de trazas predefinidas.
- Ingreso manual de trazas.
- Generación aleatoria de trazas.
- Simulación con gran cantidad de instrucciones.
- Cálculo de aciertos.
- Cálculo de tasa de aciertos.
- Visualización de resultados en tabla.
- Visualización mediante gráfica comparativa.
- Exportación de resultados a Excel.

---

## Predictores implementados

### Predict Not Taken

Estrategia estática que siempre predice que el salto no será tomado.

### Predict Taken

Estrategia estática que siempre predice que el salto será tomado.

### Predictor de 2 Bits

Estrategia dinámica que utiliza una máquina de estados para ajustar su predicción según el comportamiento anterior de la traza.

---

## Estructura del proyecto

```text
PREDICTORDESALTOS/
│
├── core/
│   ├── predictors.py
│   └── evaluator.py
│
├── gui/
│   └── app.py
│
├── utils/
│   └── generator.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Descripción general de carpetas

### `core/`

Contiene la lógica principal del sistema, incluyendo los predictores y el proceso de evaluación.

### `gui/`

Contiene la interfaz gráfica del proyecto.

### `utils/`

Contiene funciones auxiliares para generar y analizar trazas.

### `main.py`

Archivo principal para iniciar la aplicación.

### `requirements.txt`

Archivo con las dependencias necesarias para ejecutar el proyecto.

---

## Tipos de trazas disponibles

El sistema permite trabajar con diferentes tipos de trazas:

- Mayormente tomada.
- Mayormente no tomada.
- Alternada.
- Mixta.
- Aleatoria.
- Personalizada.

Estas trazas permiten observar cómo cambia el rendimiento de cada predictor dependiendo del comportamiento de los saltos.

---

## Métrica de evaluación

La métrica principal del proyecto es la **tasa de aciertos**.

La tasa de aciertos indica el porcentaje de predicciones correctas realizadas por cada estrategia.

```text
Tasa de aciertos = (Aciertos / Total de instrucciones) * 100
```

---

## Resultados mostrados

El sistema muestra los resultados en una tabla con la siguiente información:

| Columna | Descripción |
|---|---|
| Predictor | Nombre de la estrategia evaluada |
| Aciertos | Cantidad de predicciones correctas |
| Total | Total de instrucciones evaluadas |
| Tasa | Porcentaje de aciertos |

También se genera una gráfica de barras para comparar visualmente el rendimiento de los predictores.

---

## Dependencias

El proyecto utiliza las siguientes librerías:

| Librería | Uso |
|---|---|
| `customtkinter` | Interfaz gráfica |
| `matplotlib` | Gráficas comparativas |
| `pandas` | Manejo de datos tabulares |
| `openpyxl` | Exportación a Excel |

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/nombre-del-repositorio.git
```

```bash
cd nombre-del-repositorio
```

---

### 2. Crear entorno virtual

En Windows:

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

En Linux o macOS:

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución

Para ejecutar el proyecto:

```bash
python main.py
```

Al ejecutar este comando se abrirá la interfaz gráfica del sistema.

---

## Uso general

Desde la interfaz gráfica se pueden realizar las siguientes acciones:

1. Seleccionar una traza predefinida.
2. Ingresar una traza personalizada.
3. Generar una traza aleatoria.
4. Ejecutar el análisis de los predictores.
5. Visualizar los resultados en tabla.
6. Comparar los resultados mediante una gráfica.
7. Exportar los resultados a Excel.

---

## Exportación de resultados

El sistema permite exportar los resultados de la comparación en un archivo `.xlsx`.

Esta opción facilita guardar los datos obtenidos durante la simulación para su posterior análisis o presentación.

---

## Limitaciones

Este proyecto es una simulación académica y didáctica.

El predictor de 2 bits implementado representa una versión simplificada del funcionamiento real de un predictor usado en procesadores. Su objetivo es demostrar el comportamiento general de una estrategia dinámica frente a predictores estáticos.

---

## Conclusiones

El proyecto permite observar que el rendimiento de un predictor depende del comportamiento de la traza evaluada.

Los predictores estáticos pueden funcionar bien cuando el patrón de la traza es muy marcado. Por otro lado, el predictor de 2 bits puede adaptarse al comportamiento observado, aunque su rendimiento puede variar dependiendo del tipo de traza.

La predicción de saltos es una técnica importante en arquitectura de computadores porque ayuda a reducir riesgos de control y mejora el aprovechamiento del pipeline.

---

## Posibles mejoras futuras

- Agregar nuevos tipos de predictores.
- Permitir cargar trazas desde archivos externos.
- Exportar un historial más detallado de la simulación.
- Agregar más métricas de evaluación.
- Mejorar la visualización gráfica.
- Incluir comparación automática entre varias trazas.

---

## Autor

Proyecto académico desarrollado para la asignatura de Arquitectura de Computadores.

---

## Licencia

Este proyecto se desarrolló con fines educativos.