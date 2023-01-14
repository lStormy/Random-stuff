#Importado:
import random 

#Variables Globales
valores = {'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6, 
           'Siete': 7, 'Ocho': 8, 'Nueve': 9, 'Diez': 10, 'Jota': 11, 
           'Reina': 12, 'Rey': 13, 'As': 14}
palos = ('Corazones', 'Diamantes', 'Espadas', 'Picas')
numeros = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 
           'Diez', 'Jota', 'Reina', 'Rey', 'As')

#Cartas
class Carta:
    def __init__ (self, palo, numero):
        self.palo = palo
        self.numero = numero
        self.val = valores [numero]
    def valor (self):
        return (self.val)
    def __str__ (self):
        return f'{self.numero} De {self.palo}'

#Mazo
class Mazo: 
    def __init__ (self): 
        self.cartas = []
        for palo in palos:
            for numero in numeros:
                carta_creada = Carta(palo,numero)
                self.cartas.append(carta_creada)
    def mezclar (self):
        random.shuffle (self.cartas)
    def repartir_una (self):
        return self.cartas.pop()

#Jugador
class Jugador: 
    def __init__ (self,nombre):
        self.nombre = nombre
        self.en_mano = []
    def eliminar (self):
        return self.en_mano.pop(0)
    def agregar (self, nueva_carta):
        if type (nueva_carta) == type ([]):
            self.en_mano.extend (nueva_carta)
        else:    
            self.en_mano.append(nueva_carta)
    def Valor (self): 
        return self.en_mano[0]
    def __len__ (self):
        return len (self.en_mano)
    def __str__(self):
        return f'Las cartas que tiene son: {self.en_mano} '

class Mesa: 
    def __init__ (self): 
        self.cartas = []
    def agregar (self,cartas): 
        if type(cartas) == type ([]):
            self.cartas.extend(cartas)
        else: 
            self.cartas.append(cartas)
    def En_mesa(self):
        return self.cartas
    def __len__ (self):
        return len(self.cartas)
    def __str__(self): 
        return f'Las cartas en la mesa son: {self.cartas()}'

