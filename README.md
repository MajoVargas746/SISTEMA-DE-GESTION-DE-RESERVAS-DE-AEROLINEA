# SISTEMA-DE-GESTION-DE-RESERVAS-DE-AEROLINEA
Sistema de gestión de reservas de aerolínea desarrollado con Programación Orientada a Objetos, enfocado en administrar vuelos, pasajeros, asientos y reservas. Modela entidades como Persona, Pasajero, Vuelo, Asiento y Reserva, estableciendo relaciones entre clases para organizar la información y facilitar procesos de registro, asignación y control



<img width="829" height="784" alt="image" src="https://github.com/user-attachments/assets/dd78e5ca-4bb8-45b7-98ae-271ac592ac9f" />


Definición de los requisitos funcionales 

RF1- Registrar pasajero
Descripción: El sistema debe permitir registrar un pasajero con sus datos personales.
Entrada: Nombre, identificación, edad, categoría.
Salida: Confirmación de registro exitoso

Ingrese nombre:
Ingrese identificación:
Ingrese edad:
Ingrese categoría:
Pasajero registrado correctamente.

RF2 – Mostrar datos de pasajero
Descripción: El sistema debe permitir visualizar la información de un pasajero.
Salida: Datos completos del pasajero

--- DATOS DEL PASAJERO ---
Nombre: Kelli Cabrera
ID: 254056
Edad: 35
Categoría: Económica

RF3 – Crear vuelo
Descripción: Permite crear un vuelo con información básica.
Entrada: ID, hora salida, hora llegada, capacidad.
Salida: Vuelo creado.

Ingrese ID del vuelo:
Ingrese hora de salida:
Ingrese hora de llegada:
Ingrese capacidad:
Vuelo creado correctamente.

RF4 – Validar cupo de vuelo
Descripción: Verifica si el vuelo tiene disponibilidad.
Salida: Disponible / No disponible.

RF5 – Crear reserva
Descripción: Permite generar una reserva asociando pasajero, vuelo y asiento.
Entrada: Código, origen, destino, fecha, valor.
Salida: Reserva creada.

Ingrese código de reserva:
Ingrese origen:
Ingrese destino:
Ingrese fecha:
Ingrese valor:
Reserva creada correctamente.

RF6 – Asignar asiento
Descripción: Permite asignar un asiento disponible a una reserva.
Entrada: Número de asiento.
Salida: Confirmación o error si está ocupado.

RF7 – Pagar reserva
Descripción: Permite marcar una reserva como pagada.
Salida: Estado actualizado.

RF8 – Cancelar reserva
Descripción: Permite cancelar una reserva y liberar el asiento.
Salida: Confirmación de cancelación.

RF9 – Liberar asiento
Descripción: Permite liberar un asiento cuando una reserva es cancelada.

RF10 – Cambiar estado de vuelo
Descripción: Permite cambiar el estado del vuelo (activo, cancelado).


RF11 – Reservar vuelo (interacción principal)
Descripción: Permite a un pasajero realizar una reserva completa.
Incluye: validación de cupo + asignación de asiento.

RF12 – Cancelar reserva desde pasajero
Descripción: El pasajero puede cancelar su reserva directamente.
