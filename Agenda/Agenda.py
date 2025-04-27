# Abril 27 2025
# Registro de contactos guardado en archivos CSV

class Contacto():
    def __init__(self,nombre,telefono,correo,pais):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo
        self.__pais = pais

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Nombre no puede ser vacio")
        else:
            self.__nombre = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Numero no puede ser vacio")
        else:
            self.__telefono = value

    @property
    def _correo(self):
        return self.__correo

    @_correo.setter
    def _correo(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Correo no puede ser vacio")
        else:
            self.__correo = value

    @property
    def _pais(self):
        return self.__pais

    @_pais.setter
    def _pais(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Pais no puede ser vacio")
        else:
            self.__pais = value




