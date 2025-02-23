from abc import ABC , abstractmethod
import json

class Vehiculo (ABC):
    def __init__(self, placa, marca, modelo, combustible):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible

    @abstractmethod
    def estado(self):
        pass

class Moto(Vehiculo):
    def __init__(self, placa, marca, modelo, combustible, estilo):
        super().__init__(placa, marca, modelo, combustible)
        self.estilo = estilo
    
    def estado(self):
        return f"[Moto] Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Combustible: {self.combustible}, Estilo: {self.estilo}"
    
class Camion(Vehiculo):
    def __init__(self, placa, marca, modelo, combustible, carga):
        super().__init__(placa, marca, modelo, combustible)
        self.carga = carga

    def estado(self):
        return f"[Camion] Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Combustible: {self.combustible}, Carga: {self.carga}"
    
class Flota:
    def __init__(self):
        self.flotilla = []
        
    def agregar_vehiculo(self, n):
        if isinstance(n,Vehiculo):
            self.flotilla.append(n)
        else:
            print("Solo se puede agregar un vehiculo")

    def mostrar_vehiculos(self):
        if len(self.flotilla) > 0:
            for n in self.flotilla:
                print(n.estado())
        else:
            print("No hay vehiculos en la lista")

    def guardar_flota(self, archivo):
        flota_data = []
        for n in self.flotilla:
            vehiculo_info = {
                "Placa":n.placa,
                "Marca":n.marca,
                "Modelo":n.modelo,
                "Combustible":n.combustible
            
            }
            if isinstance(n,Moto):
                vehiculo_info ["Tipo"] = "Moto"
                vehiculo_info ["Estilo"] = n.estilo
            
            elif isinstance(n,Camion):
                vehiculo_info ["Tipo"] = "Camion"
                vehiculo_info ["Carga"] = n.carga

            flota_data.append(vehiculo_info)

        with open(archivo, "w") as file:
            json.dump(flota_data, file, indent=4)

        print("Informacion Guardada")

        def cargar_flota(self,archivo):
            try:
                with open(archivo, "r") as file:
                    flota_data = json.load(file)
                    for vehiculo_data in flota_data:
                        if vehiculo_data["Tipo"] == "Moto":
                            vehiculo = Moto(vehiculo_data["Placa"],vehiculo_data["Marca"],vehiculo_data["Modelo"], vehiculo_data["Combustible"],vehiculo_data["Estilo"])
                        elif vehiculo_data["Tipo"] == "Camion":
                            vehiculo = Camion(vehiculo_data["Placa"],vehiculo_data["Marca"],vehiculo_data["Modelo"], vehiculo_data["Combustible"],vehiculo_data["Carga"])
                        self.agregar_vehiculo(vehiculo)
            except FileNotFoundError:
                print(f"El Archivo {archivo} No Existe")
            except json.JSONDecodeError:
                print(f"EL Archivo {archivo} Esta En Formato Invalido")
            except:
                print(f"Ocurrio Un Error Al Intentar Abrir El Archivo {archivo}")