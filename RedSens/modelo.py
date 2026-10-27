from dataclasses import dataclass


@dataclass
class Estacion:
    codigo: str
    numero: int
    nombre: str
    localidad: str
    tipo: str
    bateria: int
    diasSinVisita: int
