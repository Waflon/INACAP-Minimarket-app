from Persona import Persona
from DAO_Persona import DAOPersona
from datetime import datetime
import requests
import json

dao = DAOPersona()

url = "https://csarivan.000webhostapp.com/repositorios/personas.json"  # Personas
r = requests.get(url)
lineas = r.text
datos = json.loads(lineas)

for registro in datos:
    rut = registro['rut']
    nombre = registro['nombre']
    direccion = registro['direccion']
    fechaNacimiento = datetime.strptime(registro['fechaNacimiento'], '%d-%m-%Y')
    comuna = registro['comuna']
    correoElectronico = registro['correoElectronico']
    persona_instancia = Persona(rut, nombre, direccion, fechaNacimiento, comuna, correoElectronico)
    dao.insertarPersona(persona_instancia)