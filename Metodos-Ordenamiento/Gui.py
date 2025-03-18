# from Burble import BubbleSort
# from Quick import QuickSort
# from Merge import MergeSort
# from Counting import CountingSort
# from Radix import RadixSort
# from Bucket import BucketSort
# from Heap import HeapSort
# from Insertion import InsertionSort
# from Selection import SelectionSort
# import tkinter as tk
# from tkinter import ttk, messagebox, font
# from Api import fetch_data
# from SortingAlgorithm import SortingAlgorithm
# from tkinter import PhotoImage
# import os
# #.



# class SortingApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sorting Algorithms - Desmovilizados y Año")
#         self.root.geometry("1200x600")

#         # Colores personalizados
#         self.colors = {
#             "background": "#1E1E2E",
#             "card_bg": "#2D2D44",
#             "text": "#FFFFFF",
#             "primary": "#6A0DAD",
#             "info": "#3498db",
#             "warning": "#f39c12",
#             "error": "#e74c3c",
#             "success": "#2ecc71"
#         }

#         # Configurar el fondo de la ventana principal
#         self.root.configure(bg=self.colors["background"])

#         # Cargar datos de la API
#         self.data = fetch_data()
#         if not self.data:
#             self.create_custom_dialog("Error", "No se pudieron obtener datos de la API.", "error")
#             self.root.destroy()
#             return

#         # Verificar las claves disponibles en los datos
#         print("Claves disponibles en los datos:", self.data[0].keys())

#         # Obtener claves numéricas automáticamente
#         self.numeric_keys = self.get_numeric_keys()
#         if not self.numeric_keys:
#             self.create_custom_dialog("Error", "No se encontraron claves numéricas en los datos.", "error")
#             self.root.destroy()
#             return

#         # Variables de control
#         self.sort_type = tk.StringVar(value="quick")
#         self.order = tk.StringVar(value="asc")
#         self.selected_key = tk.StringVar(value=self.numeric_keys[0])

#         # Crear interfaz
#         self.create_widgets()
#         self.load_data()

#     def get_numeric_keys(self):
#         # Obtener claves numéricas de los datos
#         numeric_keys = []
#         for key in self.data[0].keys():
#             try:
#                 # Intentar convertir el valor a float para ver si es numérico
#                 float(self.data[0][key])
#                 numeric_keys.append(key)
#             except (ValueError, TypeError):
#                 continue
#         return numeric_keys

#     def create_widgets(self):
#         # Frame para los controles
#         control_frame = ttk.Frame(self.root)
#         control_frame.pack(fill=tk.X, padx=10, pady=10)

#         ttk.Label(control_frame, text="Algoritmo de Ordenamiento:").grid(row=0, column=0, padx=5, pady=5)
#         ttk.Combobox(control_frame, textvariable=self.sort_type, values=["quick", "merge", "insertion", "bubble", "counting", "heap", "bucket"]).grid(row=0, column=1, padx=5, pady=5)

#         ttk.Label(control_frame, text="Orden:").grid(row=1, column=0, padx=5, pady=5)
#         ttk.Combobox(control_frame, textvariable=self.order, values=["asc", "desc"]).grid(row=1, column=1, padx=5, pady=5)

#         ttk.Label(control_frame, text="Parámetro:").grid(row=2, column=0, padx=5, pady=5)
#         ttk.Combobox(control_frame, textvariable=self.selected_key, values=self.get_pretty_numeric_keys()).grid(row=2, column=1, padx=5, pady=5)

#         ttk.Button(control_frame, text="Ordenar", command=self.sort_data).grid(row=3, column=0, columnspan=2, pady=10)

#         # Frame para la tabla
#         table_frame = ttk.Frame(self.root)
#         table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

#         # Crear el Treeview con columnas dinámicas
#         self.tree = ttk.Treeview(table_frame, columns=tuple(f"#{i+1}" for i in range(len(self.data[0].keys()))), show="headings")
        
#         # Asignar nombres de columnas como encabezados
#         column_names = self.get_pretty_column_names()
#         for i, col in enumerate(self.data[0].keys()):
#             self.tree.heading(f"#{i+1}", text=column_names.get(col, col))
#             self.tree.column(f"#{i+1}", width=150, anchor=tk.CENTER)
        
#         self.tree.pack(fill=tk.BOTH, expand=True)

#         # Aplicar colores alternados a las filas
#         self.apply_row_colors()

#     def get_pretty_column_names(self):
#         # Diccionario para mapear nombres de columnas a nombres más bonitos
#         pretty_names = {
#             "departamento": "Departamento",
#             "departamento_de_residencia_dane": "Departamento de Residencia (DANE)",
#             "anhodesmovilizacion": "Año de Desmovilización",
#             "numerodesmovilizados": "Número de Desmovilizados",
#             "fechacorte": "Fecha de Corte",
#             "fechaactualizacion": "Fecha de Actualización",
#         }
#         return pretty_names

#     def get_pretty_numeric_keys(self):
#         # Obtener nombres bonitos para las claves numéricas
#         pretty_names = self.get_pretty_column_names()
#         return [pretty_names.get(key, key) for key in self.numeric_keys]

#     def get_original_key(self, pretty_key):
#         # Obtener el nombre original de la clave a partir del nombre bonito
#         pretty_names = self.get_pretty_column_names()
#         for original, pretty in pretty_names.items():
#             if pretty == pretty_key:
#                 return original
#         return pretty_key  # Si no se encuentra, devolver el mismo valor

#     def load_data(self):
#         # Insertar datos en la tabla
#         for item in self.data:
#             self.tree.insert("", tk.END, values=list(item.values()))

#         # Aplicar colores alternados a las filas
#         self.apply_row_colors()

#     def sort_data(self):
#         sort_type = self.sort_type.get()
#         order = self.order.get()
#         pretty_key = self.selected_key.get()

#         # Obtener el nombre original de la clave
#         original_key = self.get_original_key(pretty_key)

#         ascending = order == "asc"

#         # Mapeo de algoritmos de ordenamiento
#         SortingAlgorithm = {
#             "quick": QuickSort(),
#             "merge": MergeSort(),
#             "insertion": InsertionSort(),
#             "bubble": BubbleSort(),
#             "counting": CountingSort(),
#             "heap": HeapSort(),
#             "bucket": BucketSort(),
#             "radix": RadixSort(),  # Agregar RadixSort
#             "selection": SelectionSort()
#         }

#         try:
#             # Filtrar datos para asegurarnos de que la clave seleccionada tenga valores válidos
#             filtered_data = []
#             for item in self.data:
#                 if original_key in item:
#                     try:
#                         # Intentar convertir el valor a float
#                         value = float(item[original_key])
#                         filtered_data.append(item)
#                     except (ValueError, TypeError):
#                         continue  # Ignorar elementos con valores no convertibles a float

#             if not filtered_data:
#                 self.create_custom_dialog("Advertencia", f"No hay datos válidos para ordenar por '{pretty_key}'.", "warning")
#                 return

#             # Ordenar los datos utilizando el algoritmo seleccionado
#             sorted_data = SortingAlgorithm[sort_type].sort(filtered_data, original_key, ascending)
#             self.update_table(sorted_data)
#             self.create_custom_dialog("Éxito", "Datos ordenados correctamente.", "success")
#         except Exception as e:
#             self.create_custom_dialog("Error", f"Error al ordenar los datos: {str(e)}", "error")

#     def update_table(self, sorted_data):
#         # Limpiar la tabla
#         for row in self.tree.get_children():
#             self.tree.delete(row)

#         # Insertar los datos ordenados
#         for item in sorted_data:
#             self.tree.insert("", tk.END, values=list(item.values()))

#         # Aplicar colores alternados a las filas
#         self.apply_row_colors()

#     def apply_row_colors(self):
#         """Aplica colores alternados a las filas para mejor legibilidad"""
#         for i, item in enumerate(self.tree.get_children()):
#             if i % 2 == 0:
#                 self.tree.item(item, tags=('evenrow',))
#             else:
#                 self.tree.item(item, tags=('oddrow',))
                
#         # Configurar etiquetas de fila
#         self.tree.tag_configure('evenrow', background=self.colors["card_bg"])
#         self.tree.tag_configure('oddrow', background="#3D3D4F")  # Un poco más claro que card_bg

#     def create_custom_dialog(self, title, message, type_="info"):
#         """Crea un diálogo personalizado con tema oscuro"""
#         dialog = tk.Toplevel(self.root)
#         dialog.title(title)
#         dialog.geometry("300x150")
#         dialog.resizable(False, False)
        
#         bg_color = self.colors["background"]
#         accent_color = self.colors.get(type_, self.colors["primary"])
        
#         # Configurar el diálogo
#         dialog.configure(bg=bg_color)
        
#         # Encabezado
#         header = tk.Frame(dialog, bg=accent_color, height=40)
#         header.pack(fill=tk.X)
        
#         title_label = tk.Label(header, text=title, bg=accent_color, fg=self.colors["text"], font=("Segoe UI", 12, "bold"))
#         title_label.pack(pady=10)
        
#         # Mensaje
#         msg_frame = tk.Frame(dialog, bg=bg_color)
#         msg_frame.pack(fill=tk.BOTH, expand=True)
        
#         msg_label = tk.Label(msg_frame, text=message, bg=bg_color, fg=self.colors["text"], font=("Segoe UI", 10), wraplength=280)
#         msg_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
#         # Botón
#         btn_frame = tk.Frame(dialog, bg=bg_color, height=40)
#         btn_frame.pack(fill=tk.X)
        
#         ok_btn = tk.Button(btn_frame, text="Aceptar", command=dialog.destroy, bg=accent_color, fg=self.colors["text"], 
#                         font=("Segoe UI", 9, "bold"), relief=tk.FLAT, padx=15)
#         ok_btn.pack(pady=10)
        
#         # Hacer el diálogo modal
#         dialog.transient(self.root)
#         dialog.grab_set()
#         dialog.focus_set()
        
#         return dialog
from Burble import BubbleSort
from Quick import QuickSort
from Merge import MergeSort
from Counting import CountingSort
from Radix import RadixSort
from Bucket import BucketSort
from Heap import HeapSort
from Insertion import InsertionSort
from Selection import SelectionSort
import tkinter as tk
from tkinter import ttk, messagebox, font
from Api import fetch_data
from SortingAlgorithm import SortingAlgorithm
from tkinter import PhotoImage
import os


class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithms - Desmovilizados y Año")
        self.root.geometry("1200x600")

        # Colores personalizados
        self.colors = {
            "background": "#1E1E2E",
            "card_bg": "#2D2D44",
            "text": "#FFFFFF",
            "primary": "#6A0DAD",
            "info": "#3498db",
            "warning": "#f39c12",
            "error": "#e74c3c",
            "success": "#2ecc71"
        }

        # Configurar el fondo de la ventana principal
        self.root.configure(bg=self.colors["background"])

        # Cargar datos de la API
        self.data = fetch_data()
        if not self.data:
            self.create_custom_dialog("Error", "No se pudieron obtener datos de la API.", "error")
            self.root.destroy()
            return

        # Verificar las claves disponibles en los datos
        print("Claves disponibles en los datos:", self.data[0].keys())

        # Variables de control
        self.sort_type = tk.StringVar(value="quick")
        self.order = tk.StringVar(value="asc")
        self.selected_key = tk.StringVar(value="Año de Desmovilización")  # Valor por defecto

        # Crear interfaz
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Frame para los controles
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=10, pady=10)

        # Algoritmo de Ordenamiento
        ttk.Label(control_frame, text="Algoritmo de Ordenamiento:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Combobox(
            control_frame,
            textvariable=self.sort_type,
            values=["quick", "merge", "insertion", "bubble", "counting", "heap", "bucket", "radix", "selection"]
        ).grid(row=0, column=1, padx=5, pady=5)

        # Orden (ascendente o descendente)
        ttk.Label(control_frame, text="Orden:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Combobox(control_frame, textvariable=self.order, values=["asc", "desc"]).grid(row=1, column=1, padx=5, pady=5)

        # Parámetro de ordenamiento (solo Año de Desmovilización y Número de Desmovilizados)
        ttk.Label(control_frame, text="Parámetro:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Combobox(
            control_frame,
            textvariable=self.selected_key,
            values=["Año de Desmovilización", "Número de Desmovilizados"]
        ).grid(row=2, column=1, padx=5, pady=5)

        # Botón para ordenar
        ttk.Button(control_frame, text="Ordenar", command=self.sort_data).grid(row=3, column=0, columnspan=2, pady=10)

        # Frame para la tabla
        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear el Treeview con columnas dinámicas
        self.tree = ttk.Treeview(table_frame, columns=tuple(f"#{i+1}" for i in range(len(self.data[0].keys()))), show="headings")
        
        # Asignar nombres de columnas como encabezados
        column_names = self.get_pretty_column_names()
        for i, col in enumerate(self.data[0].keys()):
            self.tree.heading(f"#{i+1}", text=column_names.get(col, col))
            self.tree.column(f"#{i+1}", width=150, anchor=tk.CENTER)
        
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Aplicar colores alternados a las filas
        self.apply_row_colors()

    def get_pretty_column_names(self):
        # Diccionario para mapear nombres de columnas a nombres más bonitos
        pretty_names = {
            "departamento": "Departamento",
            "departamento_de_residencia_dane": "Departamento de Residencia (DANE)",
            "anhodesmovilizacion": "Año de Desmovilización",
            "numerodesmovilizados": "Número de Desmovilizados",
            "fechacorte": "Fecha de Corte",
            "fechaactualizacion": "Fecha de Actualización",
        }
        return pretty_names

    def get_original_key(self, pretty_key):
        # Obtener el nombre original de la clave a partir del nombre bonito
        pretty_names = self.get_pretty_column_names()
        for original, pretty in pretty_names.items():
            if pretty == pretty_key:
                return original
        return pretty_key  # Si no se encuentra, devolver el mismo valor

    def load_data(self):
        # Insertar datos en la tabla
        for item in self.data:
            self.tree.insert("", tk.END, values=list(item.values()))

        # Aplicar colores alternados a las filas
        self.apply_row_colors()

    def sort_data(self):
        sort_type = self.sort_type.get()
        order = self.order.get()
        pretty_key = self.selected_key.get()

        # Obtener el nombre original de la clave
        original_key = self.get_original_key(pretty_key)

        ascending = order == "asc"

        # Mapeo de algoritmos de ordenamiento
        sorting_algorithms = {
            "quick": QuickSort(),
            "merge": MergeSort(),
            "insertion": InsertionSort(),
            "bubble": BubbleSort(),
            "counting": CountingSort(),
            "heap": HeapSort(),
            "bucket": BucketSort(),
            "radix": RadixSort(),
            "selection": SelectionSort()
        }

        try:
            # Filtrar datos para asegurarnos de que la clave seleccionada tenga valores válidos
            filtered_data = []
            for item in self.data:
                if original_key in item:
                    try:
                        # Intentar convertir el valor a float
                        value = float(item[original_key])
                        filtered_data.append(item)
                    except (ValueError, TypeError):
                        continue  # Ignorar elementos con valores no convertibles a float

            if not filtered_data:
                self.create_custom_dialog("Advertencia", f"No hay datos válidos para ordenar por '{pretty_key}'.", "warning")
                return

            # Ordenar los datos utilizando el algoritmo seleccionado
            sorted_data = sorting_algorithms[sort_type].sort(filtered_data, original_key, ascending)
            self.update_table(sorted_data)
            self.create_custom_dialog("Éxito", "Datos ordenados correctamente.", "success")
        except Exception as e:
            self.create_custom_dialog("Error", f"Error al ordenar los datos: {str(e)}", "error")

    def update_table(self, sorted_data):
        # Limpiar la tabla
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar los datos ordenados
        for item in sorted_data:
            self.tree.insert("", tk.END, values=list(item.values()))

        # Aplicar colores alternados a las filas
        self.apply_row_colors()

    def apply_row_colors(self):
        """Aplica colores alternados a las filas para mejor legibilidad"""
        for i, item in enumerate(self.tree.get_children()):
            if i % 2 == 0:
                self.tree.item(item, tags=('evenrow',))
            else:
                self.tree.item(item, tags=('oddrow',))
                
        # Configurar etiquetas de fila
        self.tree.tag_configure('evenrow', background=self.colors["card_bg"])
        self.tree.tag_configure('oddrow', background="#3D3D4F")  # Un poco más claro que card_bg

    def create_custom_dialog(self, title, message, type_="info"):
        """Crea un diálogo personalizado con tema oscuro"""
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("300x150")
        dialog.resizable(False, False)
        
        bg_color = self.colors["background"]
        accent_color = self.colors.get(type_, self.colors["primary"])
        
        # Configurar el diálogo
        dialog.configure(bg=bg_color)
        
        # Encabezado
        header = tk.Frame(dialog, bg=accent_color, height=40)
        header.pack(fill=tk.X)
        
        title_label = tk.Label(header, text=title, bg=accent_color, fg=self.colors["text"], font=("Segoe UI", 12, "bold"))
        title_label.pack(pady=10)
        
        # Mensaje
        msg_frame = tk.Frame(dialog, bg=bg_color)
        msg_frame.pack(fill=tk.BOTH, expand=True)
        
        msg_label = tk.Label(msg_frame, text=message, bg=bg_color, fg=self.colors["text"], font=("Segoe UI", 10), wraplength=280)
        msg_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Botón
        btn_frame = tk.Frame(dialog, bg=bg_color, height=40)
        btn_frame.pack(fill=tk.X)
        
        ok_btn = tk.Button(btn_frame, text="Aceptar", command=dialog.destroy, bg=accent_color, fg=self.colors["text"], 
                        font=("Segoe UI", 9, "bold"), relief=tk.FLAT, padx=15)
        ok_btn.pack(pady=10)
        
        # Hacer el diálogo modal
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.focus_set()
        
        return dialog