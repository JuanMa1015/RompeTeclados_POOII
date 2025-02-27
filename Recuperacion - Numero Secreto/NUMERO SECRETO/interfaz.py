import tkinter as tk 
from tkinter import messagebox
from juego import JuegoAdivinanza
from PIL import Image, ImageTk

class InterfazJuego:
    def __init__(self):
        self.juego = JuegoAdivinanza()
        self.ventana = tk.Tk()
        self.ventana.title("Adivina el Número")
        self.ventana.geometry("800x600")
        self.ventana.configure(bg="#222")
        
        # Para mantener referencias a los widgets
        self.widgets = {}
        self.historial_intentos = []  # Para guardar el historial de intentos
        
        try:
            self.cargar_fondo()
        except Exception as e:
            print(f"Error al cargar la imagen de fondo: {e}")
            # Crear un fondo alternativo si la imagen falla
            self.label_bg = tk.Label(self.ventana, bg="#222")
            self.label_bg.place(relwidth=1, relheight=1)
        
        # Llamar directamente a la pantalla inicial
        self.mostrar_pantalla_inicial()
        self.ventana.mainloop()

    def cargar_fondo(self):
        try:
            self.bg_image = Image.open("assets/fondocool.jpg")
            # Obtener dimensiones actuales
            ancho = self.ventana.winfo_width() or 800
            alto = self.ventana.winfo_height() or 600
            
            # Redimensionar la imagen
            redim = self.bg_image.resize((ancho, alto))
            self.bg = ImageTk.PhotoImage(redim)
            
            # Crear la etiqueta de fondo
            self.label_bg = tk.Label(self.ventana, image=self.bg)
            self.label_bg.place(x=0, y=0, relwidth=1, relheight=1)
            
            # Vincular el evento de redimensión de la ventana
            self.ventana.bind("<Configure>", self.on_resize)
        except Exception as e:
            print(f"No se pudo cargar la imagen de fondo: {e}")
            raise  # Reenviar la excepción para manejarla en __init__
    
    def on_resize(self, event):
        # Actualizar el fondo cuando se redimensiona la ventana
        try:
            ancho = self.ventana.winfo_width()
            alto = self.ventana.winfo_height()
            if ancho > 1 and alto > 1 and hasattr(self, 'bg_image'):  # Evitar redimensionar a tamaños inválidos
                redim = self.bg_image.resize((ancho, alto))
                self.bg = ImageTk.PhotoImage(redim)
                self.label_bg.configure(image=self.bg)
        except Exception as e:
            print(f"Error al redimensionar: {e}")

    def limpiar_ventana(self):
        # Guardar la referencia al fondo
        bg_temp = None
        if hasattr(self, 'label_bg'):
            bg_temp = self.label_bg
        
        # Destruir todos los widgets excepto el fondo
        for widget in self.ventana.winfo_children():
            if widget != bg_temp:
                widget.destroy()
        
        # Asegurarse de que el fondo esté al fondo
        if bg_temp:
            bg_temp.lower()

    def mostrar_pantalla_inicial(self):
        # Limpiar la ventana primero
        self.limpiar_ventana()
        
        # Crear un marco principal con fondo semitransparente
        main_frame = tk.Frame(self.ventana, bg="#222222", bd=5)
        main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)
        
        # Título del juego
        title_label = tk.Label(main_frame, text="Adivina el Número", 
                              font=("Arial", 24, "bold"), 
                              bg="#222222", fg="cyan",
                              pady=20)
        title_label.pack()
        
        # Marco para los datos de los jugadores
        players_frame = tk.Frame(main_frame, bg="#222222", pady=10)
        players_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Jugador 1
        player1_frame = tk.Frame(players_frame, bg="#222222", pady=10)
        player1_frame.pack(fill=tk.X)
        
        tk.Label(player1_frame, text="Nombre Jugador 1:", 
                font=("Arial", 12), fg="white", bg="#222222").pack(anchor="w")
        self.entry_jugador1 = tk.Entry(player1_frame, font=("Arial", 12), width=30)
        self.entry_jugador1.pack(fill=tk.X, pady=5)
        
        tk.Label(player1_frame, text="Número secreto de Jugador 1 (4 dígitos):", 
                font=("Arial", 12), fg="white", bg="#222222").pack(anchor="w")
        self.entry_numero_secreto1 = tk.Entry(player1_frame, show="*", font=("Arial", 12), width=30)
        self.entry_numero_secreto1.pack(fill=tk.X, pady=5)
        
        # Jugador 2
        player2_frame = tk.Frame(players_frame, bg="#222222", pady=10)
        player2_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(player2_frame, text="Nombre Jugador 2:", 
                font=("Arial", 12), fg="white", bg="#222222").pack(anchor="w")
        self.entry_jugador2 = tk.Entry(player2_frame, font=("Arial", 12), width=30)
        self.entry_jugador2.pack(fill=tk.X, pady=5)
        
        tk.Label(player2_frame, text="Número secreto de Jugador 2 (4 dígitos):", 
                font=("Arial", 12), fg="white", bg="#222222").pack(anchor="w")
        self.entry_numero_secreto2 = tk.Entry(player2_frame, show="*", font=("Arial", 12), width=30)
        self.entry_numero_secreto2.pack(fill=tk.X, pady=5)
        
        # Botón para iniciar el juego
        start_button = tk.Button(main_frame, text="Iniciar Juego", 
                               command=self.iniciar_juego, 
                               bg="cyan", fg="black",
                               font=("Arial", 14, "bold"),
                               padx=20, pady=10)
        start_button.pack(pady=20)
        
        # Poner el foco en el primer campo
        self.entry_jugador1.focus_set()

    def iniciar_juego(self):
        jugador1 = self.entry_jugador1.get().strip()
        jugador2 = self.entry_jugador2.get().strip()
        numero_secreto1 = self.entry_numero_secreto1.get().strip()
        numero_secreto2 = self.entry_numero_secreto2.get().strip()

        if not jugador1 or not jugador2:
            messagebox.showerror("Error", "Debes ingresar los nombres de los jugadores.")
            return

        if not self.juego.validar_numero_secreto(numero_secreto1):
            messagebox.showerror("Error", "El número secreto de Jugador 1 debe tener 4 dígitos y no puede empezar con 0.")
            return

        if not self.juego.validar_numero_secreto(numero_secreto2):
            messagebox.showerror("Error", "El número secreto de Jugador 2 debe tener 4 dígitos y no puede empezar con 0.")
            return

        self.juego.registrar_jugadores(jugador1, jugador2, numero_secreto1, numero_secreto2)
        self.pantalla_juego()

    def pantalla_juego(self):
        self.limpiar_ventana()
        
        # Panel principal
        panel = tk.Frame(self.ventana, bg="#222")
        panel.place(relx=0.5, rely=0.1, anchor="n", relwidth=0.9, relheight=0.8)
        
        # Título del turno actual
        self.label_turno = tk.Label(panel, text=f"Turno de {self.juego.obtener_jugador_turno()}", 
                                   font=("Arial", 18, "bold"), fg="cyan", bg="#222")
        self.label_turno.pack(pady=20)
        
        # Frame para el intento
        frame_intento = tk.Frame(panel, bg="#222")
        frame_intento.pack(pady=10)
        
        tk.Label(frame_intento, text="Ingresa tu intento (4 dígitos):", 
               fg="white", bg="#222", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.entry_intento = tk.Entry(frame_intento, width=10, font=("Arial", 12))
        self.entry_intento.pack(side=tk.LEFT, padx=5)
        self.entry_intento.focus_set()  # Poner el foco en la entrada
        
        tk.Button(frame_intento, text="Intentar", command=self.verificar_intento, 
                bg="cyan", fg="black", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        # Panel para mostrar el historial de intentos
        frame_historial = tk.Frame(panel, bg="#333", padx=10, pady=10)
        frame_historial.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Título del historial
        tk.Label(frame_historial, text="Historial de Intentos", 
               font=("Arial", 14, "bold"), fg="white", bg="#333").pack(pady=10)
        
        # Frame para el área de texto y la barra de desplazamiento
        text_frame = tk.Frame(frame_historial, bg="#333")
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        # Texto para el historial
        self.texto_intentos = tk.Text(text_frame, height=15, width=50, 
                                    bg="#111", fg="white", 
                                    font=("Courier", 12))
        self.texto_intentos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Añadir scrollbar
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configurar la barra de desplazamiento
        self.texto_intentos.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.texto_intentos.yview)
        
        # Hacer que la entrada responda a Enter
        self.entry_intento.bind("<Return>", lambda event: self.verificar_intento())

    def verificar_intento(self):
        intento = self.entry_intento.get().strip()
        if not self.juego.validar_numero_secreto(intento):
            messagebox.showerror("Error", "El intento debe ser un número de 4 dígitos y no puede empezar con 0.")
            self.entry_intento.delete(0, tk.END)
            return

        jugador_actual = self.juego.obtener_jugador_turno()
        resultado = self.juego.intentar_adivinar(intento)

        # Guardar el intento en el historial
        entrada_historial = f"{jugador_actual} intentó: {intento} -> {resultado}\n"
        self.historial_intentos.append(entrada_historial)

        # Actualizar el área de texto con todos los intentos
        self.texto_intentos.config(state="normal")
        self.texto_intentos.delete(1.0, tk.END)  # Limpiar el texto
        for entrada in self.historial_intentos:
            self.texto_intentos.insert(tk.END, entrada)
        self.texto_intentos.see(tk.END)  # Desplazarse al final
        self.texto_intentos.config(state="disabled")

        # Limpiar la entrada para el siguiente intento
        self.entry_intento.delete(0, tk.END)

        #  Si el juego ha terminado, mostrar ventana emergente y reiniciar
        if "[FIN]" in resultado:
            messagebox.showinfo("¡Fin del juego!", resultado.replace("[FIN]", "").strip())
            self.reiniciar_juego()
        else:
            # Asegurar que el turno se actualice correctamente en la interfaz
            self.actualizar_turno()


    def actualizar_turno(self):
        self.label_turno.config(text=f"Turno de {self.juego.obtener_jugador_turno()}")

    
    def reiniciar_juego(self):
        if messagebox.askyesno("Juego Terminado", "¿Quieres iniciar un nuevo juego?"):
            self.historial_intentos = []
            self.mostrar_pantalla_inicial()
        else:
            self.ventana.destroy()  # Cerrar la aplicación