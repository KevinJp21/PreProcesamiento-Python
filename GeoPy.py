from geopy.distance import geodesic

# Supongamos que esta es la ubicación del cliente
ubicacion_cliente = (37.774929, -122.419416)  # Ejemplo: San Francisco
centros_medicos = [
    {"nombre": "Centro Médico A", "direccion": "100 Main St, Nueva York, NY", "coordenadas": (40.712776, -74.005974)},
    {"nombre": "Centro Médico B", "direccion": "200 Grand Ave, Los Ángeles, CA", "coordenadas": (34.052235, -118.243683)},
    {"nombre": "Centro Médico C", "direccion": "300 Elm St, Chicago, IL", "coordenadas": (41.878113, -87.629799)}
]

def encontrar_centro_mas_cercano(ubicacion_cliente, centros_medicos):
    centro_mas_cercano = None
    distancia_minima = float('inf')

    for centro in centros_medicos:
        distancia = geodesic(ubicacion_cliente, centro["coordenadas"]).kilometers
        if distancia < distancia_minima:
            distancia_minima = distancia
            centro_mas_cercano = centro

    return centro_mas_cercano, distancia_minima  # Devolver ambos, el centro y la distancia

# Usar la función y capturar ambos valores retornados
centro_cercano, distancia_minima = encontrar_centro_mas_cercano(ubicacion_cliente, centros_medicos)
print(f"El centro médico más cercano es {centro_cercano['nombre']} a {distancia_minima:.2f} km de distancia.")