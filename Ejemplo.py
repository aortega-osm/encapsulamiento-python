class Persona:
    def __init__(self,edad,nombre,apellido):
        self._edad=edad
        self._nombre=nombre
        self._apellido=apellido

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad):
        self._edad=edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,apellido):
        self._apellido =apellido

def mostrar_detalle(self):
    print(f"Persona: {self._nombre}{self._apellido}{self._edad}")

persona1= Persona("Juan","Perez",30)
persona1.nombre="Mario"
persona1.apellido="Torres"
persona1.edad=21
