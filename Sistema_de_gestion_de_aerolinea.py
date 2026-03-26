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
    def __init__(self, numero, clase="economica"):
        self.numero = numero          
        self.clase = clase            
        self.ocupado = False
        self.pasajero = None
 
    def asignar(self, pasajero):
        if not self.ocupado:
            self.pasajero = pasajero
            self.ocupado = True
            return True
        return False
 
    def liberar(self):
        self.pasajero = None
        self.ocupado = False
 
    def __str__(self):
        estado = f"ocupado por {self.pasajero.nombre}" if self.ocupado else "libre"
        return f"Asiento {self.numero} ({self.clase}) - {estado}"
 
 
class Vuelo:
    def __init__(self, codigo, origen, destino, capacidad):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []
        self.asientos = [Asiento(str(i + 1)) for i in range(capacidad)]
 
    def tiene_espacio(self):
        return len(self.pasajeros) < self.capacidad
 
    def agregar_pasajero(self, pasajero):
        if self.tiene_espacio():
            self.pasajeros.append(pasajero)
            return True
        return False
 
    def asiento_disponible(self):
        """Retorna el primer asiento libre, o None si no hay."""
        for asiento in self.asientos:
            if not asiento.ocupado:
                return asiento
        return None
 
    def __str__(self):
        return (f"Vuelo {self.codigo}: {self.origen} -> {self.destino} "
                f"| {len(self.pasajeros)}/{self.capacidad}")
 
 
class Reserva:
    contador = 0
 
    def __init__(self, pasajero, vuelo):
        Reserva.contador += 1
        self.id = f"R{Reserva.contador}"
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.activa = True
        self.asiento = None

        
        if vuelo.agregar_pasajero(pasajero):
            asiento = vuelo.asiento_disponible()
            if asiento:
            asiento.asignar(pasajero)
            self.asiento = asiento
 
    def cancelar(self):
        self.activa = False
        self.vuelo.pasajeros.remove(self.pasajero)
        if self.asiento:
            self.asiento.liberar()
 
    def __str__(self):
        estado = "activa" if self.activa else "cancelada"
        asiento_info = f" | Asiento {self.asiento.numero}" if self.asiento else ""
        return f"[{self.id}] {self.pasajero.nombre} en {self.vuelo.codigo}{asiento_info} - {estado}"
