from Sistema_de_gestion_de_aerolinea import Pasajero, Vuelo, Reserva

# Crear pasajeros
p1 = Pasajero("Ana Torres", "CC001", 30)
p2 = Pasajero("Luis Pérez", "CC002", 22)
print(p1)
print(p2)

# Crear vuelo
v1 = Vuelo("AV101", "BOG", "MDE", 3)
print(v1)

# Crear reservas
r1 = Reserva(p1, v1)
v1.agregar_pasajero(p1)
print(r1)

r2 = Reserva(p2, v1)
v1.agregar_pasajero(p2)
print(r2)

print(v1)

# Cancelar reserva
r1.cancelar()
print(r1)
print(v1)
