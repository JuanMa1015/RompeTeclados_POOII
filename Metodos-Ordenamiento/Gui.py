from Burble import bubble_sort
from Quick import quick_sort
from Merge import merge_sort
from Counting import counting_sort
from Radix import radix_sort
from Bucket import bucket_sort
from Heap import heap_sort
from Insertion import insertion_sort
from Selection import selection_sort

import tkinter as tk
from tkinter import ttk, messagebox
from Api import fetch_data


class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithms - Desmovilizados y Año")
        self.root.geometry("1200x600")

        # Cargar datos de la API
        self.data = fetch_data()
        if not self.data:
            messagebox.showerror("Error", "No se pudieron obtener datos de la API.")
            self.root.destroy()
            return

        # Verificar las claves disponibles en los datos
        print("Claves disponibles en los datos:", self.data[0].keys())

        # Obtener claves numéricas automáticamente
        self.numeric_keys = self.get_numeric_keys()
        if not self.numeric_keys:
            messagebox.showerror("Error", "No se encontraron claves numéricas en los datos.")
            self.root.destroy()
            return

        # Variables de control
        self.sort_type = tk.StringVar(value="quick")
        self.order = tk.StringVar(value="asc")
        self.selected_key = tk.StringVar(value=self.numeric_keys[0])

        # Crear interfaz
        self.create_widgets()
        self.load_data()

    def get_numeric_keys(self):
        # Solo incluir las claves deseadas
        desired_keys = ["numerodesmovilizados", "anhodesmovilizacion"]
        numeric_keys = []
        for key in desired_keys:
            if key in self.data[0]:
                try:
                    # Intentar convertir el valor a float para ver si es numérico
                    float(self.data[0][key])
                    numeric_keys.append(key)
                except (ValueError, TypeError):
                    continue
        return numeric_keys

    def create_widgets(self):
        # Frame para los controles
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(control_frame, text="Algoritmo de Ordenamiento:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Combobox(control_frame, textvariable=self.sort_type, values=["quick", "merge", "insertion", "selection", "bubble", "counting", "heap", "radix", "bucket"]).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(control_frame, text="Orden:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Combobox(control_frame, textvariable=self.order, values=["asc", "desc"]).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(control_frame, text="Parámetro:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Combobox(control_frame, textvariable=self.selected_key, values=self.get_pretty_numeric_keys()).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(control_frame, text="Ordenar", command=self.sort_data).grid(row=3, column=0, columnspan=2, pady=10)

        # Frame para la tabla
        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear el Treeview con columnas dinámicas
        self.tree = ttk.Treeview(table_frame, columns=tuple(f"#{i+1}" for i in range(len(self.get_desired_columns()))), show="headings")
        
        # Asignar nombres de columnas como encabezados
        column_names = self.get_pretty_column_names()
        desired_columns = self.get_desired_columns()
        for i, col in enumerate(desired_columns):
            self.tree.heading(f"#{i+1}", text=column_names.get(col, col))
            self.tree.column(f"#{i+1}", width=150, anchor=tk.CENTER)
        
        self.tree.pack(fill=tk.BOTH, expand=True)

    def get_desired_columns(self):
        # Columnas que se mostrarán en la tabla
        return ["departamento", "departamento_de_residencia_dane", "anhodesmovilizacion", "numerodesmovilizados"]

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

    def get_pretty_numeric_keys(self):
        # Obtener nombres bonitos para las claves numéricas
        pretty_names = self.get_pretty_column_names()
        return [pretty_names.get(key, key) for key in self.numeric_keys]

    def get_original_key(self, pretty_key):
        # Obtener el nombre original de la clave a partir del nombre bonito
        pretty_names = self.get_pretty_column_names()
        for original, pretty in pretty_names.items():
            if pretty == pretty_key:
                return original
        return pretty_key  # Si no se encuentra, devolver el mismo valor

    def load_data(self):
        # Insertar datos en la tabla
        desired_columns = self.get_desired_columns()
        for item in self.data:
            # Filtrar solo las columnas deseadas
            filtered_item = {col: item[col] for col in desired_columns if col in item}
            self.tree.insert("", tk.END, values=list(filtered_item.values()))

    def sort_data(self):
        sort_type = self.sort_type.get()
        order = self.order.get()
        pretty_key = self.selected_key.get()

        # Obtener el nombre original de la clave
        original_key = self.get_original_key(pretty_key)

        ascending = order == "asc"

        sorting_functions = {
            "quick": quick_sort,
            "merge": merge_sort,
            "insertion": insertion_sort,
            "selection": selection_sort,
            "bubble": bubble_sort,
            "counting": counting_sort,
            "heap": heap_sort,
            "radix": radix_sort,
            "bucket": bucket_sort
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
                messagebox.showwarning("Advertencia", f"No hay datos válidos para ordenar por '{pretty_key}'.")
                return

            sorted_data = sorting_functions[sort_type](filtered_data, original_key, ascending)
            self.update_table(sorted_data)
            messagebox.showinfo("Éxito", "Datos ordenados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al ordenar los datos: {str(e)}")

    def update_table(self, sorted_data):
        # Limpiar la tabla
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar los datos ordenados
        desired_columns = self.get_desired_columns()
        for item in sorted_data:
            # Filtrar solo las columnas deseadas
            filtered_item = {col: item[col] for col in desired_columns if col in item}
            self.tree.insert("", tk.END, values=list(filtered_item.values()))


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()