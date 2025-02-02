## Projecto Biomas
## Creacion y division de biomas
## Creado por SImon Rozenstock 01-11-2024

class Plantas:
    count = 0
    def __init__(self,nombre,color,tamano,repro):
        self.__color = color
        self.__tamano = tamano
        self.__nombre = nombre
        self.__repro = repro
        
    # Getter for nombre
    def get_nombre(self):
        return self.__nombre
    
    # Setter for nombre
    def set_nombre(self, nombre):
        if len(nombre) != 0:
            self.__nombre = nombre
        else:
            raise ValueError("Nombre no puede ser vacio")
            
        # Getter for color
    def get_color(self):
        return self.__color
    
    # Setter for color
    def set_color(self, color):
        if len(color) != 0:
            self.__color = color
        else:
            raise ValueError("Color no puede ser vacio")

      # Getter for tamano
    def get_tamano(self):
        return self.__tamano
    
    # Setter for tamano
    def set_tamano(self, tamano):
        if tamano >= 0:
            self.__tamano = tamano
        else:
            raise ValueError("Tamano no puede ser vacio")

    # Getter for repro
    def get_repro(self):
        return self.__repro
    
    # Setter for repro
    def set_repro(self, repro):
        if repro == 1 or repro == 2 or repro == 3:
            self.__repro = repro
        else:
            raise ValueError("numero no valido")

class Animales:
    count = 0
    def __init__(self,nombre,color,tamano,alim):
        self.__nombre = nombre
        self.__color = color
        self.__tamano = tamano
        self.__alim = alim

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        if len(nombre) != 0:
            self.__nombre = nombre

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color = value

    def get_tamano(self):
        return self.__tamano

    def set_tamano(self, tamano):
        if tamano >= 0:
            self.__tamano = tamano

    def get_alim(self):
        return self.__alim

    def set_alim(self, alim):
        if alim == ("carnivoro") or alim == ("herbivoro") or alim == ("omnivoro"):
            self.__alim = alim

class Bioma:
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__plantas = []
        self.__animales = []

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        if len(nombre) != 0:
            self.__nombre = nombre
        else:
            raise ValueError ("El nombre no puede ser vacio")

    def get_plantas(self):
        return self.__plantas

    def get_animales(self):
        return self.__animales

    def add_plantas(self,planta):
        self.__plantas.append(planta)
    
    def edit_plantas(self,planta,posicion):
        if posicion >= 0 and posicion <= len(self.__plantas):
            self.__plantas[posicion] = planta
        else:
            raise ValueError("posicion no valida")
    
    def elim_plantas(self,posicion):
        if posicion >= 0 and posicion <= len(self.__plantas):
            del self.__plantas[posicion]
        else:
            raise ValueError("posicion no valida")

    def add_animal(self,animal):
        self.__animales.append(animal)
    
    def edit_animal(self,animal,posicion):
        if posicion >= 0 and posicion <= len(self.__animales):
            self.__animales[posicion] = animal
        else:
            raise ValueError("posicion no valida")
    
    def elim_animales(self,posicion):
        if posicion >= 0 and posicion <= len(self.__animales):
            del self.__animales[posicion]
        else:
            raise ValueError("posicion no valida")
    
    def __str__ (self):
        return (f"EL bioma {self.__nombre} tiene {len(self.__plantas)} plantas y {len(self.__animales)} animales.")

# ------------------------------------------------------------- Front End --------------------------------------------------------------------------------
 
# Menu principal
# crear biomas, editar biomas, borrar biomas, resumen total, salir
# si no hay biomas creados solo crear y salir
# cuando crea preguntar si quiere agregar cosas de una si/no
# editar lleva a lista de biomas para saber cual editar


def menu_princial(lista):
    if len(lista) > 0:
        print (f""" Biomas: {len(lista)}
        1- Crear Bioma
        2- Editar Bioma
        3- Borrar Bioma
        4- Resumen Total
        0- Salir""")
    else:
        print(""" No hay Biomas
        1- Crear Bioma
        0- Salir""")

def crear_bioma(lista):
    nombre = req_string("Ingresar nombre del bioma: ", "no puede ser vacio")
    nuevo = Bioma(nombre)
    lista.append(nuevo)

def req_string(msg,errormsg):
    retorno = ""
    while len(retorno) == 0:
        retorno = input(msg)
        if len(retorno) ==0:
            print(errormsg)
    return retorno

def agregar_planta():
    nombre = req_string("Ingrese el nombre de la planta ","el nombre no puede ser vacio")
    color  = req_string("Ingrese el color de la planta ", "no puede ser vacio")
    tamano = req_string("Ingrese el tamano de la planta ", "no puede ser vacio")
    repro = req_string("Ingrese la forma de reproduccion de la planta ", "no puede ser vacio")
    return Plantas(nombre,color,tamano,repro)

def agregar_animal():
    nombre = req_string("Ingrese el nombre del animal ","el nombre no puede ser vacio")
    color  = req_string("Ingrese el color del animal ", "no puede ser vacio")
    tamano = req_string("Ingrese el tamano del animal ", "no puede ser vacio")
    alim = req_string("Ingrese la dieta del animal ", "no puede ser vacio")
    return Plantas(nombre,color,tamano,alim)

def posicion_planta(lista):
    consecutivo = 1
    for x in lista:
        print (consecutivo,"-",x.get_nombre())
        consecutivo += 1
    y = (int(input("ingrese el numero de planta que quiere eliminar: "))-1)
    print(y)
    return y

def posicion_animal(lista):
    consecutivo = 1
    for x in lista:
        print (consecutivo,"-",x.get_nombre())
        consecutivo += 1
    y = (int(input("ingrese el numero del animal que quiere eliminar: "))-1)
    print(y)
    return y

def mostrar_plantas(lista):
    consecutivo = 1
    for n in lista:
        print(f"""{consecutivo}- Nombre: {n.get_nombre()}
Color: {n.get_color()}
Tamano: {n.get_tamano()}
Reproduccion: {n.get_repro()}
""")
        consecutivo += 1

def mostrar_animales(lista):
    consecutivo = 1
    for n in lista:
        print(f"""{consecutivo}- Nombre:" {n.get_nombre()}
Color: {n.get_color()}
Tamano: {n.get_tamano()}
Alimentacion: {n.get_alim()}
""")
        consecutivo += 1

def editar_bioma(lista):
    consecutivo = 1
    print("Biomas Actuales")
    for x in lista:
        print (consecutivo,"-",x.get_nombre())
        consecutivo += 1
    editar = -1
    while editar < 0 or editar > len(lista):
        editar = int(input("eliga el bioma que quiere editar"))
        if editar < 0 or editar > len(lista):
            print("numero invalido")
    cont = True
    bs = lista[editar -1]
    while cont:
        menu_editar(bs)
        o = (int(input("Elija una Opccion: ")))
        if o == 1:
            nombre = input("Ingresar nombre nuevo del bioma: ")
            try:
                bs.set_nombre(nombre)
            except Exception as error:
                print(error)
        elif o == 2:
            bs.add_plantas(agregar_planta())
        elif o == 3:
            bs.add_animal(agregar_animal())
        elif o == 4 and len(bs.get_plantas()) > 0:
            try:
                bs.elim_plantas(posicion_planta(bs.get_plantas()))
            except Exception as er:
                print("No se encontro la planta") 
        elif o == 5 and len(bs.get_plantas()) > 0:
            mostrar_plantas(bs.get_plantas())
        elif o == 6 and len(bs.get_animales()) > 0:
            try:
                bs.elim_animales(posicion_planta(bs.get_animales()))
            except Exception as er:
                print("No se encontro el animal")
        elif o == 7 and len(bs.get_animales()) > 0:
            mostrar_animales(bs.get_animales())
        elif o == 0:
            cont = False
        else:
            print("opcion no valida")

def menu_editar(bioma_seleccionado):
    print (f"El bioma selecionado es {bioma_seleccionado.get_nombre()}")
    print(""" Que Desea Hacer?
1- Modificar Nombre de Bioma
2- Agregar Planta
3- Agregar Animal""")
    if len(bioma_seleccionado.get_plantas()) > 0:
        print("""4- Borrar Planta
5- Mostar detalle de Planta""")
    if len(bioma_seleccionado.get_animales()) > 0:
        print("""6- Borrar Animal
7- Mostar detalle de Animal""")
    print("0- Regresar a Menu Principal")

    #agregar(P/A) borrar (P/A) editar (P/A) cambiar nombre (B) reporte (P/A) Regresar menu principal
    #TO DO!

def elim_bioma(lista):
    consecutivo = 1
    print("Biomas Actuales")
    for x in lista:
        print (consecutivo,"-",x.get_nombre())
        consecutivo += 1
    borrar = -1
    while borrar < 0 or borrar > len(lista):
        borrar = int(input("eliga el bioma que quiere borrar"))
        if borrar < 0 or borrar > len(lista):
            print("numero invalido")
    seguro = int(input("Digite 1 si esta seguro"))
    if seguro == 1:
        del lista[borrar-1]

# Menu Principal

lista_biomas = []

continuar = True

while continuar:
    menu_princial(lista_biomas)
    x = int(input("Ingresar Opcion: "))
    if x == 1:
        crear_bioma(lista_biomas)
    elif x == 2 and len(lista_biomas) > 0:
        editar_bioma(lista_biomas)
    elif x == 3 and len(lista_biomas) > 0:
        elim_bioma(lista_biomas)
    elif x == 4 and len(lista_biomas) > 0:
        consecutivo = 1
        for x in lista_biomas:
            print(f""" {consecutivo}- Bioma {x.get_nombre()}
Contiene {len(x.get_plantas())} plantas y {len(x.get_animales())} animales.
""")
    elif x == 0:
        continuar = False
        print("Adios!")
    else:
        print("Opcion no valida")

    