# Abril 27 2025
# Registro de contactos guardado en archivos CSV

import csv 

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

    

def guardar_contacto(contacto,archivo):
    with open(archivo,mode="w",newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre","Telefono","Correo","Pais"])
        for c in contacto:
            writer.writerow([c._nombre,c._telefono,c._correo,c._pais])

def cargar_contacto(archivo):
    contactos = []
    try: 
        with open(archivo,mode="r",encoding="utf-8") as file:
            reader = csv.DictWriter(file)
            for r in reader:
                contacto = Contacto(r["Nombre"],r["Telefono"],r["Correo"],r["Pais"])
                contactos.append(contacto)
    except FileNotFoundError:
        print("El archivo: {archivo} no fue encontrado")
    return contactos

def agregar_contacto(contactos):
    print("Informacion del contacto")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    correo = input("Correo: ")
    pais = input("Pais: ")

    contacto = Contacto(nombre,telefono,correo,pais)
    contactos.append(contacto)

def mostrar_contacto(contactos):
    if len(contactos) > 0:
        for idx, contacto in enumerate(contactos, 1):
            print(f"{idx}. {contacto._nombre}")
    else:
        print("Agenda Vacia")

#Prueba

nuevo = []
agregar_contacto(nuevo)
agregar_contacto(nuevo)
mostrar_contacto(nuevo)
        
    


