from dataclasses import dataclass
from Venta import Venta
import mysql.connector


@dataclass
class DAOVenta:
    # INSERT
    def insertarVenta(self, venta: Venta) -> None:
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='ventas_db')
        cursor = conexion.cursor()
        sql = "insert into ventas (id_venta, fecha_venta, valor_neto, rut_vendedor) values(%s, %s, %s, %s);"
        try:
            cursor.execute(sql, (venta.idVenta,
                                 venta.fechaVenta,
                                 venta.valorNeto,
                                 venta.rutVendedor))
            conexion.commit()
            print(f"Ingreso exitoso de venta: {venta.idVenta}")
        except:
            print("Hubo un problema procesando el código SQL")
        conexion.close()

    # LISTAR
    def listarVentas(self) -> list:
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='ventas_db')
        cursor = conexion.cursor()
        sql = 'select * from ventas'
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        lista_venta = list()  #

        for registro in filas:
            venta = Venta(registro[1], registro[2], registro[3], registro[4])
            lista_venta.append(venta)
        return lista_venta
