from abc import ABC , abstractmethod
import json

#clase padre es el empleado
#lleva: nombre, posicion, salario, identificacion

class Empleado(ABC):
    def __init__(self, nombre, posicion, salario, id):
        self.nombre = nombre
        self.posicion = posicion
        self.salario = 10
        self.id = id

    @abstractmethod
    def estado(self):
        pass

    @abstractmethod
    def pago(self):
        pass


class Finanzas(Empleado):
    def __init__(self, nombre, posicion, salario, id, ventas, comision):
        super().__init__(nombre, posicion, salario, id)
        self.comision = comision #porcentaje general sobre ventas
        self.ventas = ventas #Monto

    def estado(self):
        return f"[Finanzas] Nombre: {self.nombre}, Posicion: {self.posicion}, Salario: {self.pago()}, Comision Por Ventas: {int(self.ventas) * 0.05}, ID: {self.id}"
    
    def pago(self):
        return self.salario + int(self.ventas * self.comision)
        
    
class Mercadeo(Empleado):
    def __init__(self, nombre, posicion, salario, id, red):
        super().__init__(nombre, posicion, salario, id)
        self.red = red

    def estado(self):
        return f"[Mercadeo] Nombre: {self.nombre}, Posicion: {self.posicion}, Red: {self.red}, Salario: {self.pago()}, ID: {self.id}"
    
    def pago(self):
        return self.salario + 3
    
class Tech(Empleado):
    def __init__(self, nombre, posicion, salario, id, lenguage):
        super().__init__(nombre, posicion, salario, id)
        self.lenguage = lenguage

    def estado(self):
        return f"[Tech] Nombre: {self.nombre}, Posicion: {self.posicion}, Lenguage: {self.lenguage}, Salario: {self.pago()}, ID: {self.id}"
    
    def pago(self):
        return self.salario + 5

class Rh:
    def __init__(self):
        self.planilla = []

    def agregar_empleado(self, n):
        if isinstance(n, Empleado):
            self.planilla.append(n)
        else:
            print("Solo se puede agregar un empleado")
    
    def mostrar_planilla(self):
        if len(self.planilla) > 0:
            for n in self.planilla:
                print(n.estado())
        else:
            print("no hay nada en la lista")

    def guardar_planilla(self, archivo):
        planilla_data = []
        for n in self.planilla:
            planilla_info = {
                "Nombre":n.nombre,
                "Posicion":n.posicion,
                "Salario":n.pago(),
                "ID":n.id
            }
            if isinstance(n,Finanzas):
                planilla_info ["Tipo"] = "Finanzas"
                planilla_info ["Ventas"] = n.ventas
                planilla_info ["Comision"] = n.comision
            
            elif isinstance(n,Mercadeo):
                planilla_info ["Tipo"] = "Mercadeo"
                planilla_info ["Red"] = n.red

            elif isinstance(n,Tech):
                planilla_info ["Tipo"] = "Tech"
                planilla_info ["Lenguage"] = n.lenguage

            planilla_data.append(planilla_info)

        with open(archivo, "w") as file:
            json.dump(planilla_data, file, indent=4)

        print("Informacion Guardada")
            
    def cargar_planilla(self, archivo):
        try:
            with open(archivo, "r") as file:
                planilla_data = json.load(file)
                for emp in planilla_data:
                    if emp["Tipo"] == "Finanzas":
                        empleado = Finanzas(emp["Nombre"], emp["Posicion"], emp["Salario"], emp["ID"], emp["Ventas"], emp["Comision"])
                    elif emp["Tipo"] == "Mercadeo":
                        empleado = Mercadeo(emp["Nombre"], emp["Posicion"], emp["Salario"], emp["ID"], emp["Red"])
                    elif emp["Tipo"] == "Tech":
                        empleado = Tech(emp["Nombre"], emp["Posicion"], emp["Salario"], emp["ID"], emp["Lenguage"])
                    self.agregar_empleado(empleado)
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe.")
        except json.JSONDecodeError:
            print(f"El archivo {archivo} está en formato inválido.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el archivo: {e}")

Planilla_1 = Rh()

Empleado1 = Tech("Ramon","QA",10,"100003","Python")

Empleado2 = Finanzas("Carlos","ventas",10,"100004",20,0.5)

Empleado3 = Mercadeo("Luis", "CMO", 12, "100006", "B2B")

Planilla_1.agregar_empleado(Empleado1)
Planilla_1.agregar_empleado(Empleado2)
Planilla_1.agregar_empleado(Empleado3)

Planilla_1.mostrar_planilla()

Planilla_1.guardar_planilla("Rh.json")

Planilla_2 = Rh()

Planilla_2.cargar_planilla("Rh.json")

Planilla_2.mostrar_planilla()
