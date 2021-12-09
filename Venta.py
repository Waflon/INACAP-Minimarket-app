from dataclasses import dataclass
from datetime import datetime as dt


@dataclass
class Venta:
    idVenta: int
    fechaVenta: dt
    valorNeto: int
    rutVendedor: str

    def __init__(self, idVenta: int, fechaVenta: dt, valorNeto: int, rutVendedor: str):
        self.idVenta = idVenta
        self.fechaVenta = fechaVenta
        self.valorNeto = valorNeto
        self.rutVendedor = rutVendedor

    def mostrarDatos(self) -> None:
        print(f"idVenta {self.idVenta}")
        print(f"fechaVenta {self.fechaVenta}")
        print(f"valorNeto {self.valorNeto}")
        print(f"rutVendedor {self.rutVendedor}")