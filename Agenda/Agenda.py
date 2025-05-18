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

    def __str__(self):
        return(f"Nombre: {self._nombre}, Telefono: {self._telefono}, Correo: {self._correo}, Pais: {self._pais}")



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
            reader = csv.DictReader(file)
            for r in reader:
                contacto = Contacto(r["Nombre"],r["Telefono"],r["Correo"],r["Pais"])
                contactos.append(contacto)
    except FileNotFoundError:
        print(f"El archivo: {archivo} no fue encontrado")
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
            print(f"{idx}. {contacto}")
    else:
        print("Agenda Vacia")
    print("")

def buscar_contacto(contactos):
    x = input("Cual es el nombre del contacto que le gustaria buscar?").lower()
    encontrados = [c for c in contactos if x in c._nombre.lower()]
    if encontrados:
        for n in encontrados:
            print(n)
    else:
        print("No se encontraron contactos con ese nombre")

def editar_contacto(contactos):
    mostrar_contacto(contactos)
    try:
        opcion = int(input("Digite el numero correspondiente del contacto que le gustaria editar: "))-1
        if 0 <= opcion <= len(contactos):
            contacto = contactos[opcion]
            nuevo_nombre = input(f"Nuevo nombre: (Enter para mantener {contacto._nombre}) ") or contacto._nombre
            contacto._nombre = nuevo_nombre
            nuevo_telefono = input(f"Nuevo telefono: (Enter para mantener {contacto._telefono}) ") or contacto._telefono
            contacto._telefono = nuevo_telefono
            nuevo_correo = input(f"Nuevo correo: (Enter para mantener {contacto._correo}) ") or contacto._correo
            contacto._correo = nuevo_correo
            nuevo_pais = input(f"Nuevo pais: (Enter para mantener {contacto._pais}) ") or contacto._pais
            contacto._pais = nuevo_pais
        else:
            print("Error: Valor no dentro de las opciones")
    except ValueError:
        print("Entrada Invalida")

def eliminar_contacto(contactos):
    mostrar_contacto(contactos)
    try:
        opcion = int(input("Digite el numero correspondiente del contacto que le gustaria borrar: "))-1
        if 0 <= opcion <= len(contactos):
            contact = contactos.pop(opcion)
            print(f"El contacto {contact} fue eliminado")
        else:
            print("Error: Valor no dentro de las opciones")
    except ValueError:
        print ("Entrada Invalida")


def menu():
    archivo = "Agenda.csv"
    lista = cargar_contacto(archivo)
    while True:
        print("""1- Agregar Contacto
2- Mostrar Lista
3- Buscar Contacto
4- Editar Contacto
5- Borrar Contacto
6- Guardar y Salir
            """)
        opcion = int(input("Cual opcion le gustaria escoger? " ))
        if opcion == 1:
            agregar_contacto(lista)
        elif opcion == 2:
            mostrar_contacto(lista)
        elif opcion == 3:
            buscar_contacto(lista)
        elif opcion == 4:
            editar_contacto(lista)
        elif opcion == 5:
            eliminar_contacto(lista)
        elif opcion == 6:
            guardar_contacto(lista,archivo)
            print("Guardado con exito")
            print("Adios")
            break
        else:
            print("Opcion Invalida")


menu()


        
    


