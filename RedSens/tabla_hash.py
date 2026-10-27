
from config import HASH_CAPACITY


MARCA_BORRADO = object()


class TablaHash:
    def __init__(self):
        self.capacidad = HASH_CAPACITY
        self.tabla = [None] * self.capacidad

    def funcion_hash(self, numero):
        return numero % self.capacidad

    def insertar(self, estacion):
        posicion = self.funcion_hash(estacion.numero)
        primera_marca = None
        posiciones_revisadas = 0

        while posiciones_revisadas < self.capacidad:
            actual = self.tabla[posicion]

            if actual is MARCA_BORRADO:
                if primera_marca is None:
                    primera_marca = posicion

            elif actual is None:
                if primera_marca is not None:
                    posicion = primera_marca

                self.tabla[posicion] = estacion
                return True

            elif actual.numero == estacion.numero:
                return False

            posicion = (posicion + 1) % self.capacidad
            posiciones_revisadas += 1

        if primera_marca is not None:
            self.tabla[primera_marca] = estacion
            return True

        return False

    def buscar(self, numero):
        posicion = self.funcion_hash(numero)
        posiciones_revisadas = 0

        while posiciones_revisadas < self.capacidad:
            actual = self.tabla[posicion]

            if actual is None:
                return None

            if actual is not MARCA_BORRADO:
                if actual.numero == numero:
                    return actual

            posicion = (posicion + 1) % self.capacidad
            posiciones_revisadas += 1

        return None

    def eliminar(self, numero):
        posicion = self.funcion_hash(numero)
        posiciones_revisadas = 0

        while posiciones_revisadas < self.capacidad:
            actual = self.tabla[posicion]

            if actual is None:
                return False

            if actual is not MARCA_BORRADO:
                if actual.numero == numero:
                    self.tabla[posicion] = MARCA_BORRADO
                    return True

            posicion = (posicion + 1) % self.capacidad
            posiciones_revisadas += 1

        return False


if __name__ == "__main__":
    from modelo import Estacion

    tabla = TablaHash()

    estacion_1 = Estacion(
        codigo="CBA-0042",
        numero=42,
        nombre="Estación 42",
        localidad="Córdoba",
        tipo="METEOROLOGICA",
        bateria=80,
        diasSinVisita=5,
    )

    estacion_2 = Estacion(
        codigo="CBA-0083",
        numero=83,
        nombre="Estación 83",
        localidad="Villa María",
        tipo="PLUVIOMETRICA",
        bateria=65,
        diasSinVisita=10,
    )

    print("--- Prueba de inserción ---")
    print("Insertar estación 42:", tabla.insertar(estacion_1))
    print("Insertar estación 83:", tabla.insertar(estacion_2))

    print("\n--- Prueba de búsqueda ---")
    print("Buscar estación 42:", tabla.buscar(42))
    print("Buscar estación 83:", tabla.buscar(83))
    print("Buscar estación 100:", tabla.buscar(100))

    print("\n--- Prueba de eliminación ---")
    print("Eliminar estación 42:", tabla.eliminar(42))
    print("Buscar estación 42 después de eliminar:", tabla.buscar(42))
    print("Buscar estación 83 después de eliminar:", tabla.buscar(83))
    print("Eliminar estación 100:", tabla.eliminar(100))
