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


class Asiento:
    def __init__(self, numero, ubicacion="economica"):
        self.numero = numero
        self.ubicacion = ubicacion
        self.disponible = True

    def Asignar(self):
        if self.disponible:
            self.disponible = False 
            return True
         return False 

   def liberar(self):
       self.disponible = True

   def __str__(self):
       estado = "Disponible" if self.disponible else "ocupado"
       return f"Asiento{self.numero} - {estado}"

class Vuelo:
    def init(self, codigo, origen, destino, capacidad):
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

