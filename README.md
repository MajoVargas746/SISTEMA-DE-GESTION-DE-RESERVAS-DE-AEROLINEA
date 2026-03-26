# SISTEMA-DE-GESTION-DE-RESERVAS-DE-AEROLINEA
Sistema de gestión de reservas de aerolínea desarrollado con Programación Orientada a Objetos, enfocado en administrar vuelos, pasajeros, asientos y reservas. Modela entidades como Persona, Pasajero, Vuelo, Asiento y Reserva, estableciendo relaciones entre clases para organizar la información y facilitar procesos de registro, asignación y control



<img width="829" height="784" alt="image" src="https://github.com/user-attachments/assets/dd78e5ca-4bb8-45b7-98ae-271ac592ac9f" />


# FUNCIONAMIENTO
El sistema inicia con la creación de personas, que luego se convierten en pasajeros. A partir de esto, se crean los vuelos con un número limitado de asientos.
Cuando se realiza una reserva, el sistema automáticamente busca un asiento disponible dentro del vuelo y lo asigna al pasajero. Si no hay asientos libres, la reserva no se puede completar correctamente.
Cada reserva queda identificada con un código único y puede mantenerse activa o ser cancelada. En caso de cancelación, el asiento asignado se libera y el pasajero se elimina del vuelo.

# ESTRUCTURA DEL CODIGO
Estructura del sistema

El sistema está construido a partir de las siguientes clases:

Persona
Representa la información básica de un individuo, incluyendo nombre e identificación.

Pasajero
Hereda de Persona y agrega la edad. Es quien puede participar en vuelos y reservas.

Vuelo
Contiene la información del vuelo (código, origen, destino y capacidad). Además, gestiona la lista de pasajeros y los asientos disponibles.

Asiento
Representa un asiento dentro del vuelo. Tiene un número, una clase (por defecto económica) y un estado que indica si está ocupado o libre.

Reserva
Relaciona a un pasajero con un vuelo. Se encarga de generar automáticamente un identificador, asignar un asiento disponible y controlar si la reserva está activa o cancelada.

# RELACION ENTRE LAS CLASES 

*Un pasajero puede estar asociado a un vuelo a través de una reserva
*Un vuelo tiene varios pasajeros y asientos
*Cada reserva tiene un asiento asignado
*Los asientos pueden ocuparse y liberarse



