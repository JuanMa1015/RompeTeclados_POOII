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
from tkinter import ttk, messagebox, font
from Api import fetch_data
from tkinter import PhotoImage
import os
#.

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithms - Desmovilizados y Año")
        self.root.geometry("1200x700")
        
        # Define color palette - Dark Purple theme
        self.colors = {
            "primary": "#6A0DAD",    # Deep Purple
            "secondary": "#9370DB",  # Medium Purple
            "accent": "#E6E6FA",     # Lavender
            "background": "#1E1E2E", # Dark background
            "card_bg": "#2D2D3F",    # Slightly lighter dark for cards
            "text_light": "#FFFFFF", # White text
            "text_muted": "#AAAAAA", # Light gray text
            "success": "#4CAF50",    # Green
            "warning": "#FF9800",    # Orange
            "error": "#F44336",      # Red
            "border": "#444444"      # Border color
        }
        
        # Configure root background
        self.root.configure(bg=self.colors["background"])
        
        # Define fonts
        self.title_font = font.Font(family="Segoe UI", size=16, weight="bold")
        self.header_font = font.Font(family="Segoe UI", size=12, weight="bold")
        self.normal_font = font.Font(family="Segoe UI", size=10)
        self.button_font = font.Font(family="Segoe UI", size=10, weight="bold")
        
        # Configure ttk styles
        self.configure_styles()
        
        # Cargar datos de la API
        self.data = fetch_data()
        if not self.data:
            messagebox.showerror("Error", "No se pudieron obtener datos de la API.")
            self.root.destroy()
            return

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

    def configure_styles(self):
        # Configure ttk styles for a modern dark look
        style = ttk.Style()
        style.theme_use('clam')  # Use 'clam' as base theme
        
        # Configure colors
        style.configure("TFrame", background=self.colors["background"])
        
        # Headings
        style.configure("Heading.TLabel", 
                        font=self.header_font, 
                        background=self.colors["background"], 
                        foreground=self.colors["secondary"])
        
        # Normal labels
        style.configure("TLabel", 
                        font=self.normal_font, 
                        background=self.colors["card_bg"], 
                        foreground=self.colors["text_light"])
        
        # Label for dark background
        style.configure("Dark.TLabel", 
                        font=self.normal_font, 
                        background=self.colors["background"], 
                        foreground=self.colors["text_light"])
        
        # Combobox
        style.configure("TCombobox", 
                      font=self.normal_font)
        style.map('TCombobox', 
                  fieldbackground=[('readonly', self.colors["text_light"])],
                  selectbackground=[('readonly', self.colors["card_bg"])])
                  
        # Button
        style.configure("TButton", 
                        font=self.button_font,
                        background=self.colors["primary"],
                        foreground=self.colors["text_light"])
        style.map("TButton",
                  background=[('active', self.colors["secondary"])],
                  foreground=[('active', self.colors["text_light"])])
                  
        # Custom primary button
        style.configure("Primary.TButton", 
                        font=self.button_font,
                        background=self.colors["primary"],
                        foreground=self.colors["text_light"],
                        padding=(20, 10))
        style.map("Primary.TButton",
                  background=[('active', self.colors["secondary"])],
                  foreground=[('active', self.colors["text_light"])])
        
        # Treeview
        style.configure("Treeview", 
                        font=self.normal_font,
                        background=self.colors["card_bg"], 
                        foreground=self.colors["text_light"],
                        fieldbackground=self.colors["card_bg"],
                        rowheight=25)
        style.configure("Treeview.Heading", 
                        font=self.header_font,
                        background=self.colors["primary"], 
                        foreground=self.colors["text_light"])
        style.map("Treeview",
                  background=[('selected', self.colors["secondary"])],
                  foreground=[('selected', self.colors["text_light"])])

    def get_numeric_keys(self):
        # Solo incluir las claves deseadas
        desired_keys = ["anhodesmovilizacion", "numerodesmovilizados"]
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
        # Main container with padding
        main_container = ttk.Frame(self.root, padding="20")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # App title
        title_frame = ttk.Frame(main_container)
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(title_frame, 
                              text="Análisis de Desmovilización",
                              font=self.title_font,
                              bg=self.colors["background"],
                              fg=self.colors["secondary"])
        title_label.pack()
        
        # Control panel with border and shadow effect
        control_panel = tk.Frame(main_container, 
                               bg=self.colors["card_bg"],
                               highlightbackground=self.colors["secondary"],
                               highlightthickness=1,
                               bd=0)
        control_panel.pack(fill=tk.X, pady=(0, 20), ipady=10)
        
        # Control section title
        control_title = tk.Label(control_panel, 
                               text="Opciones de Ordenamiento",
                               font=self.header_font,
                               bg=self.colors["card_bg"],
                               fg=self.colors["text_light"])
        control_title.pack(pady=(10, 15), padx=10, anchor=tk.W)
        
        # Control grid with better spacing
        control_grid = tk.Frame(control_panel, bg=self.colors["card_bg"])
        control_grid.pack(fill=tk.X, padx=20, pady=5)
        
        # Row 1
        tk.Label(control_grid, text="Algoritmo:", bg=self.colors["card_bg"], fg=self.colors["text_light"], font=self.normal_font).grid(row=0, column=0, padx=(0, 10), pady=8, sticky=tk.W)
        algo_combo = ttk.Combobox(control_grid, 
                                 textvariable=self.sort_type, 
                                 values=["quick", "merge", "insertion", "selection", "bubble", "counting", "heap", "radix", "bucket"],
                                 width=15,
                                 state="readonly")
        algo_combo.grid(row=0, column=1, padx=5, pady=8, sticky=tk.W)
        
        tk.Label(control_grid, text="Orden:", bg=self.colors["card_bg"], fg=self.colors["text_light"], font=self.normal_font).grid(row=0, column=2, padx=(20, 10), pady=8, sticky=tk.W)
        order_combo = ttk.Combobox(control_grid, 
                                  textvariable=self.order, 
                                  values=["asc", "desc"],
                                  width=10,
                                  state="readonly")
        order_combo.grid(row=0, column=3, padx=5, pady=8, sticky=tk.W)
        
        # Row 2
        tk.Label(control_grid, text="Parámetro:", bg=self.colors["card_bg"], fg=self.colors["text_light"], font=self.normal_font).grid(row=1, column=0, padx=(0, 10), pady=8, sticky=tk.W)
        param_combo = ttk.Combobox(control_grid, 
                                  textvariable=self.selected_key, 
                                  values=self.get_pretty_numeric_keys(),
                                  width=25,
                                  state="readonly")
        param_combo.grid(row=1, column=1, padx=5, pady=8, columnspan=2, sticky=tk.W)
        
        # Sort button - moved to its own frame
        button_frame = tk.Frame(control_panel, bg=self.colors["card_bg"])
        button_frame.pack(fill=tk.X, padx=20, pady=(10, 5))
        
        sort_button = ttk.Button(button_frame, 
                               text="Ordenar Datos",
                               command=self.sort_data,
                               style="Primary.TButton")
        sort_button.pack(side=tk.RIGHT)
        
        # Table section with title
        table_section = ttk.Frame(main_container)
        table_section.pack(fill=tk.BOTH, expand=True)
        
        table_title = tk.Label(table_section, 
                             text="Resultados",
                             font=self.header_font,
                             bg=self.colors["background"],
                             fg=self.colors["text_light"])
        table_title.pack(pady=(0, 10), anchor=tk.W)
        
        # Table in a container with scrollbars
        table_container = tk.Frame(table_section, bg=self.colors["border"], padx=1, pady=1)
        table_container.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbars
        y_scrollbar = ttk.Scrollbar(table_container)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        x_scrollbar = ttk.Scrollbar(table_container, orient=tk.HORIZONTAL)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Create the Treeview with dynamic columns
        self.tree = ttk.Treeview(table_container, 
                               columns=tuple(f"#{i+1}" for i in range(len(self.get_desired_columns()))), 
                               show="headings",
                               yscrollcommand=y_scrollbar.set,
                               xscrollcommand=x_scrollbar.set)
        
        # Configure scrollbars
        y_scrollbar.config(command=self.tree.yview)
        x_scrollbar.config(command=self.tree.xview)
        
        # Assign column names as headings
        column_names = self.get_pretty_column_names()
        desired_columns = self.get_desired_columns()
        for i, col in enumerate(desired_columns):
            self.tree.heading(f"#{i+1}", text=column_names.get(col, col))
            # Adjust column widths based on content
            if "departamento" in col:
                width = 180
            elif "anho" in col:
                width = 120
            elif "fecha" in col:
                width = 150
            else:
                width = 150
            self.tree.column(f"#{i+1}", width=width, anchor=tk.W if "departamento" in col or "fecha" in col else tk.CENTER)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        status_bar = tk.Frame(main_container, bg=self.colors["primary"], height=25)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(10, 0))
        
        self.status_text = tk.Label(status_bar, 
                                   text="Listo para ordenar datos",
                                   bg=self.colors["primary"],
                                   fg=self.colors["text_light"],
                                   font=("Segoe UI", 9),
                                   pady=3)
        self.status_text.pack(side=tk.LEFT, padx=10)
        
        # Counter for records
        self.record_counter = tk.Label(status_bar, 
                                     text="",
                                     bg=self.colors["primary"],
                                     fg=self.colors["text_light"],
                                     font=("Segoe UI", 9),
                                     pady=3)
        self.record_counter.pack(side=tk.RIGHT, padx=10)

    def get_desired_columns(self):
        # Columnas que se mostrarán en la tabla
        return ["departamento", "departamento_de_residencia_dane", "anhodesmovilizacion", "numerodesmovilizados", "fechacorte", "fechaactualizacion"]

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
        numeric_options = [pretty_names.get(key, key) for key in self.numeric_keys]
        return numeric_options

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
            filtered_item = []
            for col in desired_columns:
                if col in item:
                    filtered_item.append(item[col])
                else:
                    filtered_item.append("")  # Valor vacío si no existe
            self.tree.insert("", tk.END, values=filtered_item)
        
        # Alternar colores de fila para mejor legibilidad
        self.apply_row_colors()
        
        # Update status
        self.status_text.config(text=f"Datos cargados correctamente")
        self.record_counter.config(text=f"Registros: {len(self.data)}")

    def sort_data(self):
        sort_type = self.sort_type.get()
        order = self.order.get()
        pretty_key = self.selected_key.get()

        # Update status
        self.status_text.config(text=f"Ordenando por {pretty_key} con algoritmo {sort_type}...")
        self.root.update()

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
            sort_data = []
            for item in self.data:
                if original_key in item:
                    try:
                        # Intentar convertir el valor a float
                        value = float(item[original_key])
                        sort_data.append(item)
                    except (ValueError, TypeError):
                        continue  # Ignorar elementos con valores no convertibles a float

            if not sort_data:
                raise ValueError(f"No hay datos numéricos válidos para ordenar por '{pretty_key}'")

            # Actualizar UI para mostrar que está trabajando
            self.root.config(cursor="wait")
            self.root.update()
            
            # Ordenar datos numéricos
            sorted_data = sorting_functions[sort_type](sort_data, original_key, ascending)
            
            # Actualizar tabla
            self.update_table(sorted_data)
            
            # Restaurar cursor
            self.root.config(cursor="")
            
            # Mostrar mensaje de éxito en la barra de estado
            order_text = "ascendente" if ascending else "descendente"
            self.status_text.config(text=f"Datos ordenados correctamente usando {sort_type} en orden {order_text}")
            self.record_counter.config(text=f"Registros: {len(sorted_data)}")
            
        except Exception as e:
            self.root.config(cursor="")
            self.status_text.config(text=f"Error: {str(e)}")
            messagebox.showerror("Error", f"Error al ordenar los datos: {str(e)}")

    def update_table(self, sorted_data):
        # Limpiar la tabla
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar los datos ordenados
        desired_columns = self.get_desired_columns()
        for item in sorted_data:
            # Filtrar solo las columnas deseadas
            filtered_item = []
            for col in desired_columns:
                if col in item:
                    filtered_item.append(item[col])
                else:
                    filtered_item.append("")  # Valor vacío si no existe
            self.tree.insert("", tk.END, values=filtered_item)
            
        # Alternar colores de fila para mejor legibilidad
        self.apply_row_colors()
    
    def apply_row_colors(self):
        """Aplica colores alternados a las filas para mejor legibilidad"""
        for i, item in enumerate(self.tree.get_children()):
            if i % 2 == 0:
                self.tree.item(item, tags=('evenrow',))
            else:
                self.tree.item(item, tags=('oddrow',))
                
        # Configure row tags
        self.tree.tag_configure('evenrow', background=self.colors["card_bg"])
        self.tree.tag_configure('oddrow', background="#3D3D4F")  # Slightly lighter than card_bg


    def create_custom_dialog(root, title, message, type_="info"):
        """Crea un diálogo personalizado con tema oscuro"""
        dialog = tk.Toplevel(root)
        dialog.title(title)
        dialog.geometry("300x150")
        dialog.resizable(False, False)
        
        colors = {
            "background": "#1E1E2E",
            "primary": "#6A0DAD",
            "text": "#FFFFFF",
            "info": "#3498db",
            "warning": "#f39c12",
            "error": "#e74c3c",
            "success": "#2ecc71"
        }
        
        bg_color = colors["background"]
        accent_color = colors.get(type_, colors["primary"])
        
        # Configure dialog
        dialog.configure(bg=bg_color)
        
        # Header
        header = tk.Frame(dialog, bg=accent_color, height=40)
        header.pack(fill=tk.X)
        
        title_label = tk.Label(header, text=title, bg=accent_color, fg=colors["text"], font=("Segoe UI", 12, "bold"))
        title_label.pack(pady=10)
        
        # Message
        msg_frame = tk.Frame(dialog, bg=bg_color)
        msg_frame.pack(fill=tk.BOTH, expand=True)
        
        msg_label = tk.Label(msg_frame, text=message, bg=bg_color, fg=colors["text"], font=("Segoe UI", 10), wraplength=280)
        msg_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button
        btn_frame = tk.Frame(dialog, bg=bg_color, height=40)
        btn_frame.pack(fill=tk.X)
        
        ok_btn = tk.Button(btn_frame, text="Aceptar", command=dialog.destroy, bg=accent_color, fg=colors["text"], 
                        font=("Segoe UI", 9, "bold"), relief=tk.FLAT, padx=15)
        ok_btn.pack(pady=10)
        
        # Make modal
        dialog.transient(root)
        dialog.grab_set()
        dialog.focus_set()
        
        return dialog