#Importado:
import random 

#Variables Globales
valores = {'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6, 
           'Siete': 7, 'Ocho': 8, 'Nueve': 9, 'Diez': 10, 'Jota': 11, 
           'Reina': 12, 'Rey': 13, 'As': 14}
palos = ('Corazones', 'Diamantes', 'Tréboles', 'Picas')
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
        return self.cartas.pop(0)

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
        return self.en_mano[0].valor()
    def __len__ (self):
        return len (self.en_mano)

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
        return f'Las cartas en la mesa son: {self.cartas}'

#Jugadores: 
jugador1 = Jugador ('1')
jugador2 = Jugador ('2')


            
#El juego

#repartir
mazo = Mazo()
mazo.mezclar()
for i in range(26): 
    jugador1.agregar(mazo.repartir_una())
    jugador2.agregar(mazo.repartir_una())

#Estructura del Juego
prendido = True
ronda = 0
while prendido: 
    #Verificar que no termino
    if len(jugador1) == 0:
        prendido = False
        print ('Gana jugador 2')
        break
    if len(jugador2) == 0:
        prendido = False
        print ('Gana jugador 1')
        break
    #Empezar ronda
    ronda += 1
    print (f'Esta es la ronda numero {ronda}')
    
    if jugador1.Valor() > jugador2.Valor():
        jugador1.agregar(jugador2.eliminar())
        print ('Pierde el combate jugador 2!')
        print (f'El jugador 2 tiene {len(jugador2)} cartas y el jugador 1 iene {len(jugador1)} cartas')
        continue
    
    elif jugador1.Valor() < jugador2.Valor():
        jugador2.agregar(jugador1.eliminar())
        print ('Pierde el combate jugador 1!')
        print (f'El jugador 2 tiene {len(jugador2)} cartas y el jugador 1 tiene {len(jugador1)} cartas')
        continue
    #Guerra
    else:
        guerra = True
        
        if len(jugador1) < 3 and len(jugador2) > 3:
            guerra = False
            print ('Gana jugador 2. Porque el jugador 1 no puede entrar en Guerra')
            prendido = False
            break
        
        elif len(jugador1) > 3 and len(jugador2) < 3:
            guerra = False
            print ('Gana jugador 1. Porque el jugador 2 no puede entrar en Guerra')
            prendido = False
            break
        
        elif len(jugador1) < 3 and len(jugador2) < 3:   
            if len(jugador1) > len(jugador2):
                guerra = False
                print ('Gana jugador 1. Ninguno de los dos puede entrar en Guerra pero el jugador 1 tiene más cartas')
                break
            elif len(jugador1) < len (jugador2):
                guerra = False
                print ('Gana jugador 2. Ninguno de los dos puede entrar en Guerra pero el jugador 2 tiene más cartas')
                break
            else: 
                guerra = False
                print ('Hay Empate')
                break
        
        print ('Las cartas son iguales')
        tablero = Mesa ()
        while guerra:    
            for i in range (3):
                tablero.agregar(jugador1.eliminar())
                tablero.agregar (jugador2.eliminar())
            
            if jugador1.Valor() > jugador2.Valor():
                jugador1.agregar(tablero.En_mesa())
                guerra = False
                print ('La guerra la gana el jugador 1')
                print (f'El jugador 2 tiene {len(jugador2)} cartas y el jugador 1 tiene {len(jugador1)} cartas')
                continue
            
            elif jugador2.Valor() > jugador1.Valor():
                jugador2.agregar(tablero.En_mesa())
                print ('La guerra la gana el jugador 2')
                guerra = False
                print (f'El jugador 2 tiene {len(jugador2)} cartas y el jugador 1 tiene {len(jugador1)} cartas')
                continue