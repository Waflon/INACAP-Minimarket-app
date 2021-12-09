from dataclasses import dataclass
from Usuario import Usuario
import mysql.connector


@dataclass
class DAOUsuario:
    # INSERT
    def insertarUsuario(self, usuario: Usuario):
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='ventas_db')
        cursor = conexion.cursor()
        sql = "insert into usuarios (user_id, rut, contrasenia) values(%s, %s, %s);"
        try:
            cursor.execute(sql, (usuario.id,
                                 usuario.rut,
                                 usuario.passwd))
            conexion.commit()
            print(f"ingreso Exitoso del usuario: {usuario.id}")
        except:
            print("Hubo un problema procesando el código SQL")
        conexion.close()

    # LISTAR
    def listarUsuarios(self):
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='ventas_db')
        cursor = conexion.cursor()
        sql = 'select * from usuarios'
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        lista_usuarios = list()  #

        for registro in filas:
            usuario = Usuario(registro[1], registro[2], registro[3])
            lista_usuarios.append(usuario)
        return lista_usuarios
