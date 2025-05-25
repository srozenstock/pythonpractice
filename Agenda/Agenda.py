# Abril 27 2025
# Registro de contactos guardado en archivos CSV

import csv
import re
import shutil
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm
console = Console()

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
    backup_archivo(archivo)
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

def backup_archivo(archivo):
    try:
        if archivo:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            shutil.copy(archivo,f"{archivo}_{timestamp}.bak")
            print(f"Backup Creado ({archivo}_{timestamp}.bak)")
    except Exception as e:
        print(f"Error al crear el respaldo {e}")

def agregar_contacto(contactos):
    print("Informacion del contacto")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    if not validar_telefono(telefono):
        print("formato no aceptado, volviendo a menu inicial")
        return
    correo = input("Correo: ")
    if not validar_email(correo):
        print("formato no aceptado, volviendo a menu inicial")
        return
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
            if validar_telefono(nuevo_telefono):
                contacto._telefono = nuevo_telefono
            else:
                print("fotmato no aceptado, no se realizo el cambio")
            nuevo_correo = input(f"Nuevo correo: (Enter para mantener {contacto._correo}) ") or contacto._correo
            if validar_email(nuevo_correo):
                contacto._correo = nuevo_correo
            else:
                print("fotmato no aceptado, no se realizo el cambio")
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

def validar_email(validacion):
    patron = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(patron,validacion)

def validar_telefono(telefono):
    return telefono.isdigit() and 7 <= len(telefono) <= 15

def ordenar(contactos):
    print("""Ordenar por:
1- Nombre
2- E-Mail
          """)
    n = int(input("Cual opcion gustaria escoger?: "))
    if n ==1:
        contactos.sort(key = lambda c: c._nombre.lower())
    elif n ==2:
        contactos.sort(key = lambda c: c._correo.lower())
    else:
        print ("Opcion invalida")

def menu():
    archivo = "Agenda.csv"
    lista = cargar_contacto(archivo)
    while True:
        console.print(f"""[blue]1[/blue]- Agregar Contacto
[green]2[/green]- Mostrar Lista
[red]3[/red]- Buscar Contacto
[orange]4[/orange]- Editar Contacto
[purple]5[/purple]- Borrar Contacto
[magenta]6[/magenta]- Ordenar Lista
[brown]7[/brown]- Guardar y Salir
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
            ordenar(lista)
            mostrar_contacto(lista)
        elif opcion == 7:
            guardar_contacto(lista,archivo)
            print("Guardado con exito")
            print("Adios")
            break
        else:
            print("Opcion Invalida")


menu()


        
    


