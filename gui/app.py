"""
Archivo: app.py

Este módulo contiene la interfaz gráfica del sistema Predictor de Saltos.

Funcionalidades principales:
- Permitir al usuario crear o cargar una traza
- Ejecutar los predictores
- Mostrar resultados en tabla
- Mostrar gráfica comparativa
- Exportar resultados a Excel
- Simular miles de instrucciones

Se utiliza:
- customtkinter → interfaz moderna
- matplotlib → gráficos
- pandas → manejo de datos
"""

import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox, filedialog, ttk

# Importamos la lógica del sistema
from core.evaluator import comparar_predictores
from utils.generator import (
    generar_traza_aleatoria,
    obtener_traza_predefinida,
    analizar_traza
)


class PredictorSaltosApp(ctk.CTk):
    """
    Clase principal de la aplicación gráfica.

    Hereda de CTk (CustomTkinter) y construye toda la interfaz.
    """

    def __init__(self):
        super().__init__()

        # Configuración de ventana
        self.title("Predictor de Saltos")
        self.state("zoomed")  # ventana maximizada
        self.resizable(True, True)

        # Tema visual
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Configuración de tabla (modo oscuro)
        self.configurar_estilo_tabla()

        # Variables de estado
        self.traza_actual = []
        self.resultados_actuales = []
        self.historial_actual = []
        self.canvas_grafica = None

        # Construcción de la interfaz
        self.crear_interfaz()

    # --------------------------------------------------------
    # CONFIGURACIÓN VISUAL
    # --------------------------------------------------------

    def configurar_estilo_tabla(self):
        """Configura el estilo oscuro de la tabla."""
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                        background="#2b2b2b",
                        foreground="white",
                        fieldbackground="#2b2b2b")

        style.configure("Treeview.Heading",
                        background="#1f1f1f",
                        foreground="white")

    # --------------------------------------------------------
    # INTERFAZ
    # --------------------------------------------------------

    def crear_interfaz(self):
        """Construye toda la interfaz gráfica."""

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Título
        ctk.CTkLabel(self,
                     text="Predictor de Saltos",
                     font=("Arial", 30, "bold")
                     ).grid(row=0, column=0, pady=10)

        ctk.CTkLabel(self,
                     text="Unidad 5 Python Intermedio",
                     font=("Arial", 14)
                     ).grid(row=1, column=0)

        # Contenedor principal
        frame = ctk.CTkFrame(self)
        frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=3)

        # Panel izquierdo (controles)
        left = ctk.CTkScrollableFrame(frame)
        left.grid(row=0, column=0, sticky="nsew")

        # Panel derecho (resultados)
        right = ctk.CTkFrame(frame)
        right.grid(row=0, column=1, sticky="nsew")

        self.crear_panel_controles(left)
        self.crear_panel_resultados(right)

    # --------------------------------------------------------
    # CONTROLES
    # --------------------------------------------------------

    def crear_panel_controles(self, frame):
        """Crea todos los botones e inputs."""

        ctk.CTkLabel(frame, text="Configuración", font=("Arial", 18)).pack(pady=10)

        # Selector de traza
        self.combo_trazas = ctk.CTkComboBox(
            frame,
            values=["Mayormente tomada", "Mayormente no tomada", "Alternada", "Mixta"]
        )
        self.combo_trazas.pack(pady=5)

        ctk.CTkButton(frame, text="Cargar traza",
                      command=self.cargar_traza_predefinida).pack(pady=5)

        # Entrada manual
        self.entrada_traza = ctk.CTkEntry(frame)
        self.entrada_traza.pack(pady=5)

        ctk.CTkButton(frame, text="Usar traza",
                      command=self.usar_traza_personalizada).pack(pady=5)

        # Generador
        self.entrada_cantidad = ctk.CTkEntry(frame, placeholder_text="Cantidad")
        self.entrada_cantidad.pack(pady=5)

        self.entrada_probabilidad = ctk.CTkEntry(frame, placeholder_text="Probabilidad %")
        self.entrada_probabilidad.pack(pady=5)

        ctk.CTkButton(frame, text="Generar aleatoria",
                      command=self.generar_aleatoria).pack(pady=5)

        # Acciones principales
        ctk.CTkButton(frame, text="Analizar",
                      command=self.analizar).pack(pady=10)

        ctk.CTkButton(frame, text="Simulación grande",
                      command=self.comparar_miles_datos).pack(pady=5)

        ctk.CTkButton(frame, text="Exportar Excel",
                      command=self.exportar_excel).pack(pady=5)

    # --------------------------------------------------------
    # RESULTADOS
    # --------------------------------------------------------

    def crear_panel_resultados(self, frame):
        """Crea la tabla y gráfica."""

        self.label_estadisticas = ctk.CTkLabel(frame, text="Resultados...")
        self.label_estadisticas.pack()

        # Tabla
        self.tabla = ttk.Treeview(frame,
                                  columns=("Predictor", "Aciertos", "Total", "Tasa"),
                                  show="headings")

        for col in ("Predictor", "Aciertos", "Total", "Tasa"):
            self.tabla.heading(col, text=col)

        self.tabla.pack(pady=10)

        # Área de gráfica
        self.frame_grafica = ctk.CTkFrame(frame)
        self.frame_grafica.pack(fill="both", expand=True)

    # --------------------------------------------------------
    # LÓGICA
    # --------------------------------------------------------

    def cargar_traza_predefinida(self):
        """Carga una traza desde el selector."""
        self.traza_actual = obtener_traza_predefinida(self.combo_trazas.get())

    def usar_traza_personalizada(self):
        """Convierte texto en traza."""
        entrada = self.entrada_traza.get().upper().split()

        if not entrada:
            messagebox.showerror("Error", "Traza vacía")
            return

        self.traza_actual = entrada

    def generar_aleatoria(self):
        """Genera una traza aleatoria."""
        try:
            n = int(self.entrada_cantidad.get() or 100)
            p = float(self.entrada_probabilidad.get() or 50) / 100

            self.traza_actual = generar_traza_aleatoria(n, p)

        except:
            messagebox.showerror("Error", "Valores inválidos")

    def analizar(self):
        """Ejecuta la comparación de predictores."""

        if not self.traza_actual:
            messagebox.showerror("Error", "No hay traza")
            return

        self.resultados_actuales, self.historial_actual = comparar_predictores(self.traza_actual)

        # Mostrar estadísticas
        stats = analizar_traza(self.traza_actual)
        self.label_estadisticas.configure(
            text=f"Total: {stats['total']} | T: {stats['tomados']} | N: {stats['no_tomados']}"
        )

        # Mostrar tabla
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        for r in self.resultados_actuales:
            self.tabla.insert("", "end",
                              values=(r["Predictor"], r["Aciertos"], r["Total"], r["Tasa de aciertos (%)"]))

        self.mostrar_grafica()

    def mostrar_grafica(self):
        """Dibuja la gráfica de resultados."""

        if self.canvas_grafica:
            self.canvas_grafica.get_tk_widget().destroy()

        nombres = [r["Predictor"] for r in self.resultados_actuales]
        tasas = [r["Tasa de aciertos (%)"] for r in self.resultados_actuales]

        fig, ax = plt.subplots()
        ax.bar(nombres, tasas)
        ax.set_ylim(0, 100)

        self.canvas_grafica = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        self.canvas_grafica.draw()
        self.canvas_grafica.get_tk_widget().pack(fill="both", expand=True)

    def comparar_miles_datos(self):
        """Simulación grande."""
        self.traza_actual = generar_traza_aleatoria(10000, 0.6)
        self.analizar()

    def exportar_excel(self):
        """Exporta resultados."""
        if not self.resultados_actuales:
            return

        ruta = filedialog.asksaveasfilename(defaultextension=".xlsx")

        df = pd.DataFrame(self.resultados_actuales)
        df.to_excel(ruta, index=False)


def iniciar_app():
    """Función que inicia la aplicación."""
    app = PredictorSaltosApp()
    app.mainloop()