from dataclasses import dataclass
from datetime import datetime


@dataclass
class Persona:
    rut: str
    nombre: str
    direccion: str
    fechaNacimiento: datetime
    comuna: str
    correoElectronico: str

    def __init__(self, rut: str, nombre: str, direccion: str, fechaNacimiento: datetime, comuna: str, correoElectronico: str):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.fechaNacimiento = fechaNacimiento
        self.comuna = comuna
        self.correoElectronico = correoElectronico

    def mostrarDatos(self) -> None:
        print(f"rut: {self.rut}") 
        print(f"nombre: {self.nombre}")
        print(f"direccion: {self.direccion}") 
        print(f"fechaNacimiento: {self.fechaNacimiento}")
        print(f"comuna: {self.comuna}")
        print(f"correoElectronico: {self.correoElectronico}")