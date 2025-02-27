import tkinter as tk
from tkinter import messagebox, simpledialog
from jugador import Jugador

class Juego:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Adivinar el Número Secreto")
        
        # Pedir nombres de los jugadores
        self.jugador1 = self.pedir_nombre_jugador("Jugador 1")
        self.jugador2 = self.pedir_nombre_jugador("Jugador 2")
        
        self.turno_actual = self.jugador1
        self.jugador1_gano = False  # Bandera para saber si el Jugador 1 ganó primero
        self.crear_interfaz()

    def pedir_nombre_jugador(self, jugador_default):
        nombre = ""
        while nombre.strip() == "":
            nombre = simpledialog.askstring("Nombre del Jugador", f"Ingresa el nombre de {jugador_default}:")
            if nombre is None:  # Si el usuario cierra la ventana, se asigna un nombre por defecto
                nombre = jugador_default
        return Jugador(nombre)

    def crear_interfaz(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.label_turno = tk.Label(self.frame, text=f"Turno de {self.turno_actual.nombre}", font=("Arial", 14))
        self.label_turno.pack()

        self.label_instruccion = tk.Label(self.frame, text="Ingresa un número de 4 dígitos (no puede empezar con 0):", font=("Arial", 12))
        self.label_instruccion.pack()

        self.entrada_numero = tk.Entry(self.frame, font=("Arial", 12))
        self.entrada_numero.pack(pady=10)

        self.boton_adivinar = tk.Button(self.frame, text="Adivinar", command=self.adivinar, font=("Arial", 12))
        self.boton_adivinar.pack(pady=10)

        self.texto_historico = tk.Text(self.frame, height=10, width=50, font=("Arial", 12))
        self.texto_historico.pack(pady=10)

        self.establecer_numeros_secretos()

    def establecer_numeros_secretos(self):
        self.jugador1.establecer_numero_secreto(self.pedir_numero_secreto(self.jugador1))
        self.jugador2.establecer_numero_secreto(self.pedir_numero_secreto(self.jugador2))

    def pedir_numero_secreto(self, jugador):
        numero = ""
        while not jugador.validar_numero(numero):
            numero = simpledialog.askstring("Número Secreto", f"{jugador.nombre}, elige tu número secreto de 4 dígitos (no puede empezar con 0):")
            if numero is None:  # Si el usuario cierra la ventana, se asigna un número por defecto
                numero = "1234"
        return numero

    def adivinar(self):
        numero_adivinado = self.entrada_numero.get()
        if not self.turno_actual.validar_numero(numero_adivinado):
            messagebox.showerror("Error", "Número inválido. Debe ser un número de 4 dígitos y no puede empezar con 0.")
            return

        if self.turno_actual == self.jugador1:
            oponente = self.jugador2
        else:
            oponente = self.jugador1

        coincidencias = oponente.adivinar_numero(numero_adivinado)
        self.texto_historico.insert(tk.END, f"{self.turno_actual.nombre} adivinó: {numero_adivinado} - Coincidencias: {coincidencias}\n")

        if numero_adivinado == oponente.numero_secreto:
            if self.turno_actual == self.jugador1:
                self.jugador1_gano = True  # El Jugador 1 ganó primero
                messagebox.showinfo("Ganador", f"{self.jugador1.nombre} ha adivinado el número secreto de {self.jugador2.nombre}.")
                self.cambiar_turno()
                self.label_turno.config(text=f"Turno de {self.turno_actual.nombre}")
                messagebox.showinfo("Turno Extra", f"{self.jugador2.nombre} tiene un turno más para empatar.")
            else:
                if self.jugador1_gano:
                    messagebox.showinfo("Empate", f"{self.jugador2.nombre} ha adivinado el número secreto de {self.jugador1.nombre}. El juego termina en empate.")
                else:
                    messagebox.showinfo("Ganador", f"{self.jugador2.nombre} ha adivinado el número secreto de {self.jugador1.nombre}. ¡{self.jugador2.nombre} gana!")
                self.root.quit()
        else:
            if self.jugador1_gano and self.turno_actual == self.jugador2:
                # Si el Jugador 1 ya ganó y el Jugador 2 falla en su intento adicional, el Jugador 1 gana
                messagebox.showinfo("Ganador", f"{self.jugador2.nombre} no ha adivinado. ¡{self.jugador1.nombre} gana!")
                self.root.quit()
            else:
                self.cambiar_turno()
                self.label_turno.config(text=f"Turno de {self.turno_actual.nombre}")

        self.entrada_numero.delete(0, tk.END)

    def cambiar_turno(self):
        if self.turno_actual == self.jugador1:
            self.turno_actual = self.jugador2
        else:
            self.turno_actual = self.jugador1