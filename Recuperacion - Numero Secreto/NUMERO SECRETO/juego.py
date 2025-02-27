class JuegoAdivinanza:
    def __init__(self):
        self.numeros_secretos = {}  # Guarda el número de cada jugador
        self.jugadores = []
        self.turno_actual = None
        self.ganador_parcial = None  # Indica si el Jugador 1 ganó parcialmente
        
    def registrar_jugadores(self, jugador1, jugador2, numero1, numero2):
        self.jugadores = [jugador1, jugador2]
        self.numeros_secretos[jugador1] = numero1
        self.numeros_secretos[jugador2] = numero2
        self.turno_actual = jugador1  # Empieza el Jugador 1
        self.ganador_parcial = None  # Reiniciar estado

    def validar_numero_secreto(self, numero):
        return numero.isdigit() and len(numero) == 4 and numero[0] != "0"

    def obtener_jugador_turno(self):
        return self.turno_actual

    def cambiar_turno(self):
        self.turno_actual = self.jugadores[1] if self.turno_actual == self.jugadores[0] else self.jugadores[0]
    
    def intentar_adivinar(self, intento):
        if not self.validar_numero_secreto(intento):
            return "Número inválido, debe ser 4 dígitos y no iniciar con 0."

        oponente = self.jugadores[1] if self.turno_actual == self.jugadores[0] else self.jugadores[0]
        numero_secreto = self.numeros_secretos[oponente]

        if intento == numero_secreto:
            if self.turno_actual == self.jugadores[0]:  # Jugador 1 gana primero
                self.ganador_parcial = self.jugadores[0]
                self.cambiar_turno()
                return f"¡{self.jugadores[0]} ha ganado parcialmente! {self.jugadores[1]}, tienes un intento para empatar."
            elif self.ganador_parcial:  # Jugador 2 empata en su último intento
                return f"¡Empate! Ambos jugadores adivinaron correctamente. [FIN]"
            else:  # Jugador 2 gana directamente
                return f"¡Felicidades {self.jugadores[1]}! Ganaste, el número era {numero_secreto}. [FIN]"

        # Si el Jugador 2 falla su intento después de que el Jugador 1 ganó
        if self.ganador_parcial and self.turno_actual == self.jugadores[1]:
            return f"¡{self.jugadores[0]} gana! {self.jugadores[1]} no logró empatar. [FIN]"

        # Calcular coincidencias para feedback
        coincidencias = sum(1 for i in range(4) if intento[i] == numero_secreto[i])

        # Solo cambiar turno si no se ha definido un ganador
        if not self.ganador_parcial or self.turno_actual != self.jugadores[1]:
            self.cambiar_turno()

        return f"Coinciden {coincidencias} número(s) exactamente."
        