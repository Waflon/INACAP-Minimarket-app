from DAO_Venta import DAOVenta
from Venta import Venta
from datetime import datetime
import multiline

dao = DAOVenta()

with open('ventas.json') as ventas:
    datos = multiline.load(ventas, multiline=True)


for registro in datos:
    idVenta = registro['idVenta']
    fechaVenta = datetime.strptime(registro['fechaVenta'], '%d-%m-%Y')
    valorNeto = registro['valorNeto']
    rutVendedor = registro['rutVendedor']
    venta_instancia = Venta(idVenta, fechaVenta, valorNeto, rutVendedor)
    dao.insertarVenta(venta_instancia)
