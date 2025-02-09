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