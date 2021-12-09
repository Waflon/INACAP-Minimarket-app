from Usuario import Usuario
from DAO_Usuario import DAOUsuario
import requests
import json

dao = DAOUsuario()

url = "https://csarivan.000webhostapp.com/repositorios/usuarios.json"  # Personas
r = requests.get(url)
lineas = r.text
datos = json.loads(lineas)

# Crear lista Usuarios
for registro in datos:
    id = registro['id']
    rut = registro['rut']
    passwd = registro['pass']
    usuario_instancia = Usuario(id, rut, passwd)
    dao.insertarUsuario(usuario_instancia)
