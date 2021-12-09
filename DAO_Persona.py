from dataclasses import dataclass
from Persona import Persona
import mysql.connector


@dataclass
class DAOPersona:
    # INSERT
    def insertarPersona(self, persona: Persona) -> None:
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='ventas_db')
        cursor = conexion.cursor()
        sql = "insert into personas (rut, nombre, direccion, fecha_nacimiento, comuna, correo_electronico) values(%s, %s, %s, %s, %s, %s);"
        try:
            cursor.execute(sql, (persona.rut,
                                 persona.nombre,
                                 persona.direccion,
                                 persona.fechaNacimiento,
                                 persona.comuna,
                                 persona.correoElectronico))
            conexion.commit()
            print(f"ingreso Exitoso de: {persona.nombre}")
        except:
            print("Hubo un problema procesando el código SQL")
        conexion.close()

    # LISTAR
    def listarPersonas(self) -> list:
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='ventas_db')
        cursor = conexion.cursor()
        sql = 'select * from personas'
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        lista_persona = list()  #

        for registro in filas:
            persona = Persona(registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
            lista_persona.append(persona)
        return lista_persona
