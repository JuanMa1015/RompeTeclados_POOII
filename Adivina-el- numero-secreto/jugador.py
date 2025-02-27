class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numero_secreto = None
        self.intentos = []

    def establecer_numero_secreto(self, numero):
        if self.validar_numero(numero):
            self.numero_secreto = numero
            return True
        else:
            return False

    def validar_numero(self, numero):
        if not numero.isdigit() or len(numero) != 4 or numero[0] == '0':
            return False
        return True

    def adivinar_numero(self, numero):
        self.intentos.append(numero)
        return self.calcular_coincidencias(numero)

    def calcular_coincidencias(self, numero):
        coincidencias = 0
        # Convertir ambos números a conjuntos para encontrar dígitos comunes
        digitos_secreto = set(self.numero_secreto)
        digitos_adivinado = set(numero)
        # Contar cuántos dígitos del número adivinado están en el número secreto
        coincidencias = len(digitos_secreto.intersection(digitos_adivinado))
        return coincidencias

    def mostrar_historico(self):
        historico = ""
        for intento in self.intentos:
            coincidencias = self.calcular_coincidencias(intento)
            historico += f"Intento: {intento} - Coincidencias: {coincidencias}\n"
        return historico