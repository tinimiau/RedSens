
from config import (
    RANDOM_SEED,
    HASH_CAPACITY,
    CREW_BASE,
    JOSEPHUS_M,
    CRITICAL_BATTERY,
)

from simulacion import generar_secuencia, verificar_semillas, comprobar_uniformidad, medir_tiempo, generar_estacion, generar_estaciones, verificar_estaciones_reproducibles, generar_mediciones, guardar_mediciones, verificar_archivo_mediciones, verificar_mediciones_reproducibles



def main():
    print("=== RedSens | Sistema de monitoreo ===")
    print("Grupo: 9")
    print(f"Semilla aleatoria: {RANDOM_SEED}")
    print(f"Capacidad inicial de la tabla hash: {HASH_CAPACITY}")
    print(f"Base del equipo: {CREW_BASE}")
    print(f"Parámetro de Josephus: {JOSEPHUS_M}")
    print(f"Batería crítica: menor que {CRITICAL_BATTERY}%")

    print("\n--- Prueba de simulación ---")

    secuencia = generar_secuencia(5, RANDOM_SEED)

    print(f"Secuencia generada: {secuencia}")
    verificar_semillas()
    comprobar_uniformidad(10000, RANDOM_SEED)
    print("\n--- Medición de tiempo ---")

    resultado, tiempo_ns = medir_tiempo(
        generar_secuencia, 10000, RANDOM_SEED
    )

    print(f"Valores generados: {len(resultado)}")
    print(f"Tiempo de generación: {tiempo_ns} ns")

    import random

    generador = random.Random(RANDOM_SEED)
    estacion = generar_estacion(1, generador)

    print("\n--- Estación simulada ---")
    print(estacion)

    print("\n--- Prueba de generación de estaciones ---")

    estaciones = generar_estaciones(3, RANDOM_SEED)

    for estacion in estaciones:
        print(estacion)
    verificar_estaciones_reproducibles(100, RANDOM_SEED)        
    estaciones = generar_estaciones(100, RANDOM_SEED)
    mediciones = generar_mediciones(5, estaciones, RANDOM_SEED)

    print("\n--- Mediciones de prueba ---")

    for linea in mediciones:
        print(linea)
    estaciones = generar_estaciones(100, RANDOM_SEED)
    mediciones = generar_mediciones(5000, estaciones, RANDOM_SEED)

    guardar_mediciones(mediciones, "mediciones.txt")

    print("\nArchivo de mediciones generado: mediciones.txt")
    print(f"Cantidad de líneas: {len(mediciones)}")
    verificar_archivo_mediciones("mediciones.txt", 5000)
    verificar_mediciones_reproducibles(
        5000, estaciones, RANDOM_SEED
    )


if __name__ == "__main__":
    main()
