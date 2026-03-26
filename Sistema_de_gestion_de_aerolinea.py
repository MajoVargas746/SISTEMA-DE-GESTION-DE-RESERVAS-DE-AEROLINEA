class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def __str__(self):
        return f"{self.nombre} ({self.identificacion})"


class Pasajero(Persona):
    def __init__(self, nombre, identificacion, edad):
        super().__init__(nombre, identificacion)
        self.edad = edad

    def __str__(self):
        return super().__str__() + f" - {self.edad} años"

        

class Vuelo:
    def __init__(self, codigo, origen, destino, capacidad):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []

    def tiene_espacio(self):
        return len(self.pasajeros) < self.capacidad

    def agregar_pasajero(self, pasajero):
        if self.tiene_espacio():
            self.pasajeros.append(pasajero)
            return True
        return False

    def str(self):
        return f"Vuelo {self.codigo}: {self.origen} -> {self.destino} | {len(self.pasajeros)}/{self.capacidad}"


class Reserva:
    contador = 0

    def init(self, pasajero, vuelo):
        Reserva.contador += 1
        self.id = f"R{Reserva.contador}"
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.activa = True

    def cancelar(self):
        self.activa = False
        self.vuelo.pasajeros.remove(self.pasajero)

    def str(self):
        estado = "activa" if self.activa else "cancelada"
        return f"[{self.id}] {self.pasajero.nombre} en {self.vuelo.codigo} - {estado}"

