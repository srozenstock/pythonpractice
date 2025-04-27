## Projecto de Magia
## Creado por Simon Rozenstock 3-12-2024

## No finalizado, flata front end

import random as rd

class Base:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__vida = 150
        self.__fuerza = 5
        self.__inteligencia = 3
        self.__stamina = 10
        self.__defensa = 1

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, nombre):
        if len(nombre) != 0:
            self.__nombre = nombre.upper()
        else:
            raise ValueError ("El nombre no puede ser vacio")

    @property
    def _vida(self):
        return self.__vida

    @_vida.setter
    def _vida(self, vida):
        if vida >= 0:
            self.__vida = vida
        else:
            self.__vida = 0

    @property
    def _fuerza(self):
        return self.__fuerza

    @_fuerza.setter
    def _fuerza(self, fuerza):
        if fuerza >= 0:
            self.__fuerza = fuerza
        else:
            raise ValueError ("Numero tiene que ser positivo") 

    @property
    def _inteligencia(self):
        return self.__inteligencia

    @_inteligencia.setter
    def _inteligencia(self, inteligencia):
        if inteligencia >= 0:
            self.__inteligencia = inteligencia
        else:
            raise ValueError ("Numero tiene que ser positivo")

    @property
    def _stamina(self):
        return self.__stamina

    @_stamina.setter
    def _stamina(self, stamina):
        if stamina >= 0:
            self.__stamina = stamina
        else:
            raise ValueError ("Numero tiene que ser positivo")
        
    @property
    def _defensa(self):
        return self.__defensa

    @_defensa.setter
    def _defensa(self, defensa):
        if defensa >= 0:
            self.__defensa = defensa
        else:
            raise ValueError ("Numero tiene que ser positivo")
        
    def ataque_fisico(self):
        if self.__stamina > 0:
            self.__stamina = self.__stamina -1
            return self.__fuerza
        else:
            return 1

    def ataque_magico(self):

        if self.__stamina > 0:
            self.__stamina = self.__stamina - 1
            return self.__inteligencia
        else:
            return 1

    def estado(self):
        return (f"{self.__nombre} - Salud: {self.__vida} - Stamina: {self.__stamina}")

    def ataque(self):
        rng = rd.randint(1,100)
        if rng >= 50: 
             print(f"{self.__nombre}Ataque Magico")
             return self.ataque_magico() 
        else:
            print(f"{self.__nombre}Ataque Fisico")
            return self.ataque_fisico()
        
    
class Guerrero(Base):
    
    def ataque_fisico(self):
        if self._stamina > 0:
            self._stamina = self._stamina -1
            self._fuerza = rd.randint(15,20)
            return self._fuerza 
        else:
            return 1
    
    def ataque_magico(self):
        if self._stamina > 0:
            self._stamina = self._stamina - 1
            self._inteligencia = rd.randint(5,10)
            return self._inteligencia 
        else:
            return 1
        
    def ataque(self):
        rng = rd.randint(1,100)
        if rng >= 70: 
            n = self.ataque_magico() 
            print(f"{self._nombre} Ataque Magico: {n}")
            return n
        else:
            n = self.ataque_fisico()
            print(f"{self._nombre} Ataque Fisico {n}")
            return n
        
class Mago(Base):
    def ataque_fisico(self):
        if self._stamina > 0:
            self._stamina = self._stamina -1
            self._fuerza = rd.randint(5,10)
            return self._fuerza 
        else:
            return 1
    
    def ataque_magico(self):
        if self._stamina > 0:
            self._stamina = self._stamina - 1
            self._inteligencia = rd.randint(15,20)
            return self._inteligencia 
        else:
            return 1
        
    def ataque(self):
        rng = rd.randint(1,100)
        if rng >= 30: 
             n = self.ataque_magico() 
             print(f"{self._nombre} Ataque Magico: {n}")
             return n
        else:
            n = self.ataque_fisico()
            print(f"{self._nombre} Ataque Fisico: {n}")
            return n

class Arquero(Base):
    def ataque_fisico(self):
        if self._stamina > 0:
            self._stamina = self._stamina -1
            self._fuerza = rd.randint(6,10)
            return self._fuerza 
        else:
            return 1
    
    def ataque_magico(self):
        if self._stamina > 0 and self.__flechas > 0:
            self._stamina = self._stamina - 1
            self._flechas = self._flechas -1
            self._inteligencia = rd.randint(8,15)
            return self._inteligencia 
        else:
            return 0

    def __init__(self, nombre):
        super().__init__(nombre)
        self.__flechas = 7

    def estado(self):
        return (f"{self.__nombre} - Salud: {self.__vida} - Stamina: {self.__stamina} - Flechas: {self.__flechas}")


    @property
    def _flechas(self):
        return self.__flechas

    @_flechas.setter
    def _flechas(self, value):
        if value > 0:
            self.__flechas = value
        else: 
            raise ValueError ("agregar numero arriba de 0")
        
    def ataque(self):
        rng = rd.randint(1,100)
        if rng >= 30 and self.__flechas > 0: 
            n = self.ataque_magico() 
            print(f"{self._nombre} Ataque Magico: {n}")
            return n
        else:
            n = self.ataque_fisico()
            print(f"{self._nombre}Arquero Ataque Fisico: {n}")
            return n

def pelea(pers_1,pers_2):

    control = 1
    while pers_1._vida > 0 and pers_2._vida > 0:
        print(f"Ronda {control}")
        print(pers_1.estado())
        print(pers_2.estado())
        rng = rd.randint(1,2)
        vida1 = pers_1._vida
        vida2 = pers_2._vida
        if rng == 1:
            ataque1 = pers_1.ataque()
            pers_2._vida = vida2 - ataque1
            if pers_2._vida > 0:
                ataque2 = pers_2.ataque()
                pers_1._vida = vida1 - ataque2
            else:
                print("Victoria de Personaje 1")
        else:
            ataque2 = pers_2.ataque()
            pers_1._vida = vida1 - ataque2
            if pers_1._vida > 0:
                ataque1 = pers_1.ataque()
                pers_2._vida = vida2 - ataque1
            else:
                print(f"Victoria de Personaje 2")
        control += 1
        

Guerrero1 = Guerrero("Azul")
Mago1 = Mago("Rojo")
pelea(Guerrero1, Mago1)