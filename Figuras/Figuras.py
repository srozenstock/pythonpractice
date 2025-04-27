## Se debe crear un programa utilizando POO que permita:
## -Crear una clase padre llamada Figura, que reciba 1 parámetro para la cantidad de lados. 
## -Crear al menos 3 clases hijas (Padre Figura), llamadas Circulo, Cuadrado, Triangulo (pueden crearse más) que cada una reciban sus parámetros particulares. 
##-Se deberá forzar que exista el método GetPerimetro y GetArea en cada Clase Hija, ya que en cada caso tiene un cálculo particular y no podrá ser compartido por la lógica de la clase padre. (método abstracto) 
##-Se guardará la información del programa en archivos, se creará un archivo con la información de cada figura con el nombre "[Nombre de la clase].json "
##-Al iniciar el programa se deberá cargar automáticamente la información de los archivos. Hay que tomar en cuenta que puede ser posible que no existan alguno de los archivos. 
##-El Front End nos permitirá las siguientes opciones:
	#* Crear Figura
	#* Mostrar detalle de todas las Figura
	#* Mostrar la cantidad de objetos existente por Figura
	#* Guardar la información en archivo.
##-Cada Clase creada deberá validar cada uno de los datos recibidos por parámetro para evitar almacenar información inconsistente.

from abc import ABC , abstractmethod
import json

class Figura(ABC):
    def __init__(self,lados):
        if lados > 0:
            self.lados = lados
        else:
            raise ValueError ("Lados no validos")
        
    @abstractmethod
    def GetPerimero(self):
        pass

    @abstractmethod
    def GetArea(self):
        pass

    @abstractmethod
    def estado(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__(1)
        if radio > 0:
            self.radio = radio
        else:
            raise ValueError ("Radio debe ser positivo")
        
    def GetArea(self):
        area = 3.1416*self.radio*self.radio
        return area
    def GetPerimero(self):
        perimetro = 2*3.1416*self.radio
        return perimetro
    def estado(self):
        return (f"Circulo de area:{self.GetArea()} y perimetro {self.GetPerimero()}")
    
class Triangulo(Figura):
    def __init__(self,base,altura):
        super().__init__(3)
        if base > 0 and altura > 0:
            self.base = base
            self.altura = altura
        else:
            raise ValueError ("Base y altura deben ser positivos")
        
    def GetArea(self):
        area = (self.base*self.altura)/2
        return area
    def GetPerimero(self):
        perimetro = 3*self.base
        return perimetro
    def estado(self):
        return (f"Triangulo de area:{self.GetArea()} y perimetro {self.GetPerimero()}")
    
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__(4)
        if lado > 0:
            lado = self.lados
        else:
            raise ValueError ("Los lados deben ser positivos")
    
    def GetArea(self):
        area = self.lados*self.lados
        return area
    def GetPerimero(self):
        perimetro = 4*self.lados
        return perimetro
    def estado(self):
        return (f"Cuadrado de area:{self.GetArea()} y perimetro {self.GetPerimero()}")
    
class Geometria:
    def __init__(self):
        self.lista = []

    def agregar_figura(self,n):
        if isinstance(n,Figura):
            self.lista.append(n)
        else:
            print("la figura no cumple con los parametros")

    def mostrar_figura(self):
        if len(self.lista) > 0:
            for n in self.lista:
                print(n.estado())
        else:
            print("No hay figuras en la lista")

    def guardar_figura(self):
        circulo_data = []
        triangulo_data = []
        cuadrado_data = []
        
        for n in self.lista:
            figura_info = {
                "Lados":n.lados
            }
            
            if isinstance(n, Circulo):
                figura_info ["Radio"] = n.radio
                circulo_data.append(figura_info)

            elif isinstance(n, Triangulo):
                figura_info ["Base"] = n.base
                figura_info ["Altura"] = n.altura
                triangulo_data.append(figura_info)

            elif isinstance(n, Cuadrado):
                figura_info ["Lado"] = n.lados
                cuadrado_data.append(figura_info)
                
        with open("Circulo.json", "w") as file:
            json.dump(circulo_data, file, indent=4)

        with open("Triangulo.json", "w") as file:
            json.dump(triangulo_data, file, indent=4)

        with open("Cuadrado.json", "w") as file:
            json.dump(cuadrado_data, file, indent=4)

        print("Informacion Guardada")

    def cargar_circulo(self, nombre = "Circulo.json"):
        try: 
            with open(nombre, "r") as file:
                circ_data = json.load(file)
                for circulo_data in circ_data:
                    circulo = Circulo(circulo_data["Radio"])
                self.agregar_figura(circulo)
        except FileNotFoundError:
            print(f"El Archivo {nombre} No Existe")
        except json.JSONDecodeError:
            print(f"EL Archivo {nombre} Esta En Formato Invalido")
        except Exception as error:
            print(f"Ocurrio Un Error Al Intentar Abrir El Archivo {nombre},{error}")

    def cargar_triangulo(self, nombre = "Triangulo.json"):
        try: 
            with open(nombre, "r") as file:
                tri_data = json.load(file)
                for triangulo_data in tri_data:
                    triangulo = Triangulo(triangulo_data["Base"],triangulo_data["Altura"])
                self.agregar_figura(triangulo)
        except FileNotFoundError:
            print(f"El Archivo {nombre} No Existe")
        except json.JSONDecodeError:
            print(f"EL Archivo {nombre} Esta En Formato Invalido")
        except Exception as error:
            print(f"Ocurrio Un Error Al Intentar Abrir El Archivo {nombre},{error}")

    def cargar_cuadrado(self, nombre = "Cuadrado.json"):
        try: 
            with open(nombre, "r") as file:
                cuad_data = json.load(file)
                for cuadrado_data in cuad_data:
                    cuadrado = Cuadrado(cuadrado_data["Lado"])
                self.agregar_figura(cuadrado)
        except FileNotFoundError:
            print(f"El Archivo {nombre} No Existe")
        except json.JSONDecodeError:
            print(f"EL Archivo {nombre} Esta En Formato Invalido")
        except Exception as error:
            print(f"Ocurrio Un Error Al Intentar Abrir El Archivo {nombre},{error}")

geometria_1 = Geometria()

triangulo1 = Triangulo(15,5)

triangulo2 = Triangulo(12,6)

circulo1 = Circulo(30)

cuadrado1 = Cuadrado(4)

geometria_1.agregar_figura(triangulo1)
geometria_1.agregar_figura(triangulo2)
geometria_1.agregar_figura(circulo1)
geometria_1.agregar_figura(cuadrado1)

geometria_1.mostrar_figura()

geometria_1.guardar_figura()

geometria2 = Geometria()

geometria2.cargar_circulo()
geometria2.cargar_cuadrado()
geometria2.cargar_triangulo()

geometria2.mostrar_figura()