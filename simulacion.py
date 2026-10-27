import random
import time
from config import RANDOM_SEED

def generar_secuencia(cantidad, semilla):
    generador = random.Random(semilla)
    secuencia = []

    for i in range(cantidad):
        numero = generador.randint(0, 100)
        secuencia.append(numero)

    return secuencia


def verificar_semillas():
    secuencia_1 = generar_secuencia(10, RANDOM_SEED)
    secuencia_2 = generar_secuencia(10, RANDOM_SEED)
    secuencia_3 = generar_secuencia(10, RANDOM_SEED + 1)

    mismas_semillas_iguales = secuencia_1 == secuencia_2
    distintas_semillas_distintas = secuencia_1 != secuencia_3

    print("\n--- Verificación de semillas ---")
    print(f"Misma semilla produce misma secuencia: {mismas_semillas_iguales}")
    print(f"Semillas distintas producen secuencias distintas: {distintas_semillas_distintas}")

    return mismas_semillas_iguales and distintas_semillas_distintas


def comprobar_uniformidad(cantidad, semilla):
    baterias = generar_secuencia(cantidad, semilla)

    intervalos = {
        "0-19": 0,
        "20-39": 0,
        "40-59": 0,
        "60-79": 0,
        "80-100": 0,
    }

    for bateria in baterias:
        if bateria <= 19:
            intervalos["0-19"] += 1
        elif bateria <= 39:
            intervalos["20-39"] += 1
        elif bateria <= 59:
            intervalos["40-59"] += 1
        elif bateria <= 79:
            intervalos["60-79"] += 1
        else:
            intervalos["80-100"] += 1

    print("\n--- Uniformidad de baterías ---")
    print(f"Cantidad de valores generados: {cantidad}")

    for intervalo, apariciones in intervalos.items():
        print(f"{intervalo}%: {apariciones} apariciones")

def medir_tiempo(funcion, *args):
    inicio = time.perf_counter_ns()

    resultado = funcion(*args)

    fin = time.perf_counter_ns()

    tiempo_transcurrido = fin - inicio

    return resultado, tiempo_transcurrido

 
from modelo import Estacion


LOCALIDADES = [
    "Córdoba",
    "Villa Carlos Paz",
    "Alta Gracia",
    "Jesús María",
    "Río Tercero",
    "Villa María",
    "San Francisco",
    "Cosquín",
    "La Falda",
    "Deán Funes",
    "Villa Dolores",
    "Río Cuarto",
]

TIPOS_ESTACION = [
    "PLUVIOMETRICA",
    "METEOROLOGICA",
    "HIDROMETRICA",
]


def generar_estacion(numero, generador):
    codigo = f"CBA-{numero:04d}"
    nombre = f"Estación {numero}"

    localidad = generador.choice(LOCALIDADES)
    tipo = generador.choice(TIPOS_ESTACION)
    bateria = generador.randint(0, 100)
    dias_sin_visita = generador.randint(0, 365)

    estacion = Estacion(
        codigo=codigo,
        numero=numero,
        nombre=nombre,
        localidad=localidad,
        tipo=tipo,
        bateria=bateria,
        diasSinVisita=dias_sin_visita,
    )

    return estacion

def generar_estaciones(cantidad, semilla):
    generador = random.Random(semilla)
    estaciones = []

    for numero in range(1, cantidad + 1):
        estacion = generar_estacion(numero, generador)
        estaciones.append(estacion)

    return estaciones

def verificar_estaciones_reproducibles(cantidad, semilla):
    estaciones_1 = generar_estaciones(cantidad, semilla)
    estaciones_2 = generar_estaciones(cantidad, semilla)

    iguales = estaciones_1 == estaciones_2

    print("\n--- Reproducibilidad de estaciones ---")
    print(f"Las listas son idénticas: {iguales}")

    return iguales

def generar_mediciones(cantidad, estaciones, semilla):
    generador = random.Random(semilla)
    lineas = []

    for i in range(cantidad):
        estacion = generador.choice(estaciones)

        dia = generador.randint(1, 28)
        fecha = f"2026-10-{dia:02d}"
        hora = f"{generador.randint(0, 23):02d}:00"

        temperatura = generador.uniform(-5, 40)
        humedad = generador.randint(0, 100)
        precipitacion = generador.uniform(0, 50)

        linea = (
            f"{estacion.codigo};{fecha};{hora};"
            f"T={temperatura:.1f};H={humedad};"
            f"P={precipitacion:.1f};BAT={estacion.bateria}"
        )

        lineas.append(linea)

    return lineas

def guardar_mediciones(mediciones, ruta):
    with open(ruta, "w", encoding="utf-8") as archivo:
        for linea in mediciones:
            archivo.write(linea + "\n")

def verificar_archivo_mediciones(ruta, cantidad_esperada):
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    cantidad_correcta = len(lineas) == cantidad_esperada
    formato_correcto = all(
        len(linea.strip().split(";")) == 7
        for linea in lineas
    )

    print("\n--- Verificación del archivo ---")
    print(f"Cantidad de líneas correcta: {cantidad_correcta}")
    print(f"Formato de siete campos correcto: {formato_correcto}")

    return cantidad_correcta and formato_correcto


def verificar_mediciones_reproducibles(cantidad, estaciones, semilla):
    mediciones_1 = generar_mediciones(cantidad, estaciones, semilla)
    mediciones_2 = generar_mediciones(cantidad, estaciones, semilla)
    mediciones_3 = generar_mediciones(cantidad, estaciones, semilla + 1)

    mismas_semillas_iguales = mediciones_1 == mediciones_2
    distintas_semillas_distintas = mediciones_1 != mediciones_3

    print("\n--- Reproducibilidad de mediciones ---")
    print(f"Misma semilla produce mediciones idénticas: {mismas_semillas_iguales}")
    print(f"Semillas distintas producen mediciones diferentes: {distintas_semillas_distintas}")

    return mismas_semillas_iguales and distintas_semillas_distintas
