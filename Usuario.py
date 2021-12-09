from dataclasses import dataclass


@dataclass
class Usuario:
    id: int
    rut: str
    passwd: str

    def __init__(self, id: int, rut: str, passwd: str):
        self.id = id
        self.rut = rut
        self.passwd = passwd

    def mostrarDatos(self) -> None:
        print(f"id = {self.id}")
        print(f"rut = {self.rut}")
        print(f"passwd = {self.passwd}")